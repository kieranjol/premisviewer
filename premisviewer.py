#!/usr/bin/env python

import lxml.etree as ET
import sys
import os
import subprocess

def get_representation_info(input, premis, premis_namespace):

    # some hacks in here for incorrectly formatted premis xml :((
    sequence = False
    category_list = premis.xpath('//ns:objectCategory',namespaces={'ns': premis_namespace})
    root_uuid = ''
    for category in category_list:
        if category.text =='representation':
            representation_root =  category.getparent()
            representation_uuid = representation_root.xpath(".//ns:objectIdentifier/ns:objectIdentifierValue[../ns:objectIdentifierType='UUID']",namespaces={'ns': premis_namespace})[0].text
            relationship_subtypes = representation_root.xpath('//ns:relationshipSubType',namespaces={'ns': premis_namespace})
            for subtype in relationship_subtypes:
                if subtype.text == 'has source':
                    source_id =  subtype.findtext('../ns:relatedObjectIdentifier/ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
                    source_id_type = subtype.findtext('../ns:relatedObjectIdentifier/ns:relatedObjectIdentifierType',namespaces={'ns': premis_namespace})
                    # hack for invalid premis docs that I'd previously created :(
                    if source_id == None:
                        source_id =  source_relationship_root.findtext('ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
                    print "%-*s   : %s" % (30,'relationshipType', 'derivation')
                    print "%-*s   : %s" % (30,'relationshipSubType', 'has source')
                    print "%-*s   : %s" % (30,'objectIdentifierType', source_id_type)
                    print "%-*s   : %s" % (30,'objectIdentifierValue', source_id)
            included_files = representation_root.xpath("ns:relationship[ns:relationshipSubType='includes']",namespaces={'ns': premis_namespace})
            format_list = []
            included_format =  premis.xpath("//ns:formatName" ,namespaces={'ns': premis_namespace})
            for i in included_format:
                if i.text not in format_list:
                    format_list.append(i.text)

            image_list, audio_list = link_uuids_to_formats(input, premis, premis_namespace, format_list)
            format_dict= {}
            for i in format_list:
                count =  len(premis.xpath("//ns:formatDesignation[ns:formatName='%s' ]" % i,namespaces={'ns': premis_namespace}))
                format_dict[i] = count
            # http://stackoverflow.com/a/17392569
            inputs  = ["%-*s   : %s, %s" % (30,'includes',v, k) for v, k in format_dict.items()]
            print '***'
            for f in inputs:
                print f
            image_sequence_uuid = representation_root.xpath("ns:relationship[ns:relationshipSubType='has root']",namespaces={'ns': premis_namespace})
            if len(image_sequence_uuid) > 0:
                if not image_sequence_uuid[0] in ['', None]:
                    root_uuid = image_sequence_uuid[0].findtext('ns:relatedObjectIdentifier/ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
                    if root_uuid == None:
                        root_uuid = image_sequence_uuid[0].findtext('ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
                    print "%-*s   : %s" % (30,'image sequence root uuid',root_uuid)
                    sequence = True
                    file_format =  premis.xpath("//ns:formatName[../../../..//ns:objectIdentifierValue='%s' ]" % root_uuid,namespaces={'ns': premis_namespace})
                    image_count =  len(premis.xpath("//ns:formatDesignation[ns:formatName='%s' ]" % file_format[0].text,namespaces={'ns': premis_namespace}))
        else:
            continue
    return sequence, format_dict, image_list, audio_list, root_uuid, representation_uuid
def get_ids(object_type, input, premis, premis_namespace):
    category_list = premis.xpath("//ns:objectCategory", namespaces={'ns': premis_namespace})
    for category in category_list:
        if category.text == object_type:
            print "%-*s   : %s" % (30,'objectCategory', object_type)
            root = category.getparent()
            identifier_list = root.xpath('ns:objectIdentifier',namespaces={'ns': premis_namespace})
            for i in identifier_list:
                id_tag = i.findtext('ns:objectIdentifierType',namespaces={'ns': premis_namespace})
                id_text = i.findtext('ns:objectIdentifierValue',namespaces={'ns': premis_namespace})

                print "%-*s   : %s" % (30,'objectIdentifierType', id_tag)
                print "%-*s   : %s" % (30,'objectIdentifierValue', id_text)
            print '\n***'


def list_agents(input, premis, premis_namespace):
    all_agent_values = premis.xpath('//ns:agentIdentifierValue',namespaces={'ns': premis_namespace})
    agent_dict = {}
    for i in all_agent_values:
        agent_dict[i.text] = i.getparent().getparent().findtext('ns:agentName',namespaces={'ns': premis_namespace})
        #agent_dict[i.text] = doc.xpath(i.getparent().i.getparent() + '//ns:agentName',namespaces={'ns': premis_namespace})
    return agent_dict

def list_events(agent_dict, input, premis, premis_namespace, image_list, audio_list, root_uuid, representation_uuid):
    # event_dict is used as a lookup refrence for list_agents
    all_events = premis.xpath('//ns:event',namespaces={'ns': premis_namespace})
    all_event_uuids = premis.xpath('//ns:eventIdentifierValue',namespaces={'ns': premis_namespace})
    event_dict = {}
    for i in all_event_uuids:
            event_dict[i.text] = i.getparent().getparent().findtext('ns:eventDetailInformation/ns:eventDetail',namespaces={'ns': premis_namespace})
    blank = 'n'
    print '\n**Events**\n'
    for i in all_events:

         print "%-*s   : %s" % (30,'eventType',  i.findtext('ns:eventType',namespaces={'ns': premis_namespace}))
         print "%-*s   : %s" % (30,'eventDate',  i.findtext('ns:eventDateTime',namespaces={'ns': premis_namespace}))
         print "%-*s   : %s" % (30,'eventDetail',  i.findtext('ns:eventDetailInformation/ns:eventDetail',namespaces={'ns': premis_namespace}))
         counter = 1
         for x in i.findall('ns:linkingAgentIdentifier/ns:linkingAgentIdentifierValue',namespaces={'ns': premis_namespace}):
             print "%-*s   : %s" % (30,'agentName',  agent_dict[x.text])
         linkingobjects = i.findall('.//ns:linkingObjectIdentifierValue',namespaces={'ns': premis_namespace})
         objectlist = []

         for objects in linkingobjects:
             objectlist.append(objects.text)

         if sorted(objectlist) == sorted(image_list):
             print "%-*s   : %s" % (30,'linkingObjectIdentifier',  'Entire Image Sequence - UUID of root : %s' % root_uuid)
         elif sorted(objectlist) == sorted(audio_list):
             print "%-*s   : %s" % (30,'linkingObjectIdentifier',  'Audio file with UUID : %s' % audio_list[0])
         elif sorted(objectlist)[0] == representation_uuid:

             print "%-*s   : %s" % (30,'linkingObjectIdentifier',  'Entire representation with UUID : %s' % representation_uuid)
         print '\n'

    return event_dict
def link_uuids_to_formats(input, premis, premis_namespace, format_list):
    format_uuid = {}
    objectlist1 = []
    objectlist2 = []
    all_formats = premis.xpath("//ns:objectIdentifierValue[..//ns:objectIdentifierType='UUID']" ,namespaces={'ns': premis_namespace})
    for i in all_formats:
        format_uuid[i.text] = i.findtext('../..//ns:formatName',namespaces={'ns': premis_namespace})
    for x in format_uuid:
        if format_uuid[x] == format_list[0]:

            objectlist1.append(x)
        elif len(format_list) > 1:
            if format_uuid[x] ==  format_list[1]:
                objectlist2.append(x)
        else:
            return objectlist1, objectlist2
    # I'm making an assumption that there will be more dpx/tiff files than audio files.
    if len(objectlist1) > len(objectlist2):
        image_list = objectlist1
        audio_list = objectlist2
    elif len(objectlist2) > len(objectlist1):
        image_list = objectlist2
        audio_list = objectlist1
    return image_list, audio_list


def print_agents(event_dict, input , premis, premis_namespace):
    all_agents = premis.xpath('//ns:agent',namespaces={'ns': premis_namespace})
    print '\n**Agents**\n'
    for i in all_agents:

        print "%-*s   : %s" % (30,'agentName',  i.findtext('ns:agentName',namespaces={'ns': premis_namespace}))
        print "%-*s   : %s" % (30,'agentType',  i.findtext('ns:agentType',namespaces={'ns': premis_namespace}))
        for x in i.findall('ns:linkingEventIdentifier/ns:linkingEventIdentifierValue',namespaces={'ns': premis_namespace}):
            try:
                print "%-*s   : %s" % (30,'eventName',  event_dict[x.text])
            except KeyError:
                print "**ERROR - %s recorded as linked event, but the event description is not in this XML document" % x.text
        print '\n'


def find_premis(input):
    xml_list = []
    if os.path.isfile(input):
        return input
    else:
        for root, dirs, files in os.walk(input):
            for filename in files:
                if filename.endswith('.xml'):
                    parser      = ET.XMLParser(remove_blank_text=True)
                    try:
                        doc         = ET.parse(os.path.join(root,filename), parser=parser)
                        cpl_namespace = doc.xpath('namespace-uri(.)')
                        if cpl_namespace == "http://www.loc.gov/premis/v3":
                            xml_list.append(os.path.join(root,filename))
                    except: SyntaxError,TypeError
        if len(xml_list) == 0:
            print 'No PREMIS version 3 XML documents found. Exiting.'
            sys.exit()
        elif len(xml_list) == 1:
            print 'returning', os.path.join(root, filename)
            return os.path.join(root, filename)

        elif len(xml_list) > 1:
            try:
                chosen_xml = choose_xml(xml_list)
            except NameError:
                print 'Enter a number!!'
                chosen_xml = choose_xml(xml_list)
            return chosen_xml

def choose_xml(xml_list):
    xml_number = 1
    chosen_xml = ''
    print '\nMultiple PREMIS XML documents found:'
    for i in xml_list:
        print xml_number,  os.path.basename(i)
        xml_number += 1
    print '\nPlease select which PREMIS XML document that you would like to process by entering the corresponding number and pressing ENTER'
    chosen_xml = input()
    print type(chosen_xml)

    return xml_list[chosen_xml -1]

def create_premis_object(input):
    """Creates an lxml PREMIS object that will be analysed by other functions.

    Args:
        input: filename string that is returned from find_premis()
    Returns:
        premis: premis lxml object
        premis_namespace: XML namespace for PREMIS v3.
    """
    parser      = ET.XMLParser(remove_blank_text=True)
    doc         = ET.parse(input,parser=parser)
    premis      = doc.getroot()
    premis_namespace    = "http://www.loc.gov/premis/v3"
    return premis, premis_namespace


def pull_all_metadata(object, counter):

    #object is a lxml element object that acts as your starting xpath point.
    #counter allows for the loop to run only a certain number of times
    all_descendants = list(object.getparent().getparent().getparent().iter())
    blank = 'n'
    for i in all_descendants:
        if i.text == None:
            if blank == 'n':
                print '\n'
                blank = 'y'
        else:
                blank = 'n'
                print "%-*s  :  %s" % (30,i.tag.replace('{http://www.loc.gov/premis/v3}',''),  i.text)
    return counter


def get_file_level(input,premis, premis_namespace, sequence, format_dict):
    print '***'
    print "\n\n%-*s   : %s" % (30,'objectCategory',  'file')
    if sequence == True:

        format_type_list = premis.xpath("//ns:formatName", namespaces={'ns': premis_namespace})
        for format_type in format_dict:
            if format_dict[format_type] == 1:
                for image_object in format_type_list:
                        if image_object.text == format_type:

                            pull_all_metadata(image_object, 1)

            elif format_dict[format_type] > 1:
                print 'Image sequence detected, only showing information about the first image object'
                counter = 1
                for image_object in format_type_list:
                    while counter == 1:
                        if image_object.text == format_type:
                            print '\n******FIRST FILE IMAGE OBJECT DOCUMENTATION******\n'
                            counter = pull_all_metadata(image_object, counter)
                            print '\n******END OF FIRST FILE IMAGE OBJECT DOCUMENTATION******\n'
                            counter += 1


def main():
    input = find_premis(sys.argv[1])
    print 'Human Readable Premis Report\n'
    premis, premis_namespace = create_premis_object(input)
    get_ids('intellectual entity',input, premis, premis_namespace)
    get_ids('representation',input, premis, premis_namespace)
    sequence, format_dict, image_list, audio_list, root_uuid, representation_uuid = get_representation_info(input,premis, premis_namespace)
    get_file_level(input,premis, premis_namespace, sequence, format_dict)
    agent_dict = list_agents(input,premis, premis_namespace)
    event_dict = list_events(agent_dict, input,premis, premis_namespace, image_list, audio_list, root_uuid, representation_uuid)
    print_agents(event_dict, input,premis, premis_namespace)


if __name__ == '__main__':
    main()
