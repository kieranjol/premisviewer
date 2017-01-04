#!/usr/bin/env python

import lxml.etree as ET
import sys
import os
import subprocess

def get_representation_info(input, premis, premis_namespace):
    print 'Human Readable Premis Report\n'
    print '**Summary Report **\n'
    # some hacks in here for incorrectly formatted premis xml :((
    category_list = premis.xpath('//ns:objectCategory',namespaces={'ns': premis_namespace})
    for category in category_list:
        if category.text =='representation':

            representation_root =  category.getparent()
            if representation_root.xpath('//ns:relationshipSubType',namespaces={'ns': premis_namespace})[0].text == 'has source':
                source_relationship_root = representation_root.xpath('//ns:relationshipSubType',namespaces={'ns': premis_namespace})[0].getparent()
                source_id =  source_relationship_root.findtext('ns:relatedObjectIdentifier/ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
                # hack for invalid premis docs that I'd previously created :(
                if source_id == None:
                    source_id =  source_relationship_root.findtext('ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
                print "%-*s   : %s" % (25,'has source', source_id)
            included_files = representation_root.xpath("ns:relationship[ns:relationshipSubType='includes']",namespaces={'ns': premis_namespace})
            included_count = len (included_files)
            format_list = []
            included_format =  premis.xpath("//ns:formatName" ,namespaces={'ns': premis_namespace})
            for i in included_format:
                if i.text not in format_list:
                    format_list.append(i.text)

            format_dict = {}
            for i in format_list:
                count =  len(premis.xpath("//ns:formatDesignation[ns:formatName='%s' ]" % i,namespaces={'ns': premis_namespace}))
                format_dict[i] = count
            # http://stackoverflow.com/a/17392569
            inputs  = ['%s: %s' % (v, k) for k, v in format_dict.items()]
            print 'Representation includes:', ' '.join(inputs)
            image_sequence_uuid = representation_root.xpath("ns:relationship[ns:relationshipSubType='has root']",namespaces={'ns': premis_namespace})
            if len(image_sequence_uuid) > 0:
                if not image_sequence_uuid[0] in ['', None]:
                    root_uuid = image_sequence_uuid[0].findtext('ns:relatedObjectIdentifier/ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
                    if root_uuid == None:
                        root_uuid = image_sequence_uuid[0].findtext('ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
                    print "%-*s   : %s" % (25,'image sequence root uuid',root_uuid)
                    file_format =  premis.xpath("//ns:formatName[../../../..//ns:objectIdentifierValue='%s' ]" % root_uuid,namespaces={'ns': premis_namespace})
                    image_count =  len(premis.xpath("//ns:formatDesignation[ns:formatName='%s' ]" % file_format[0].text,namespaces={'ns': premis_namespace}))
        else:
            continue

def get_intellectual_entity(input, premis, premis_namespace):
    category_list = premis.xpath('//ns:objectCategory',namespaces={'ns': premis_namespace})
    for category in category_list:
        if category.text =='intellectual entity':
            print '***Intellectual Entity***\n'
            category
            print "%-*s   : %s" % (25,'objectIdentifierType', source_id)
            
            

def list_agents(input, premis, premis_namespace):
    all_agent_values = premis.xpath('//ns:agentIdentifierValue',namespaces={'ns': premis_namespace})
    agent_dict = {}
    for i in all_agent_values:
        agent_dict[i.text] = i.getparent().getparent().findtext('ns:agentName',namespaces={'ns': premis_namespace})
        #agent_dict[i.text] = doc.xpath(i.getparent().i.getparent() + '//ns:agentName',namespaces={'ns': premis_namespace})
    return agent_dict

def list_events(agent_dict, input, premis, premis_namespace):
    all_events = premis.xpath('//ns:event',namespaces={'ns': premis_namespace})
    all_event_uuids = premis.xpath('//ns:eventIdentifierValue',namespaces={'ns': premis_namespace})
    event_dict = {}
    for i in all_event_uuids:
            event_dict[i.text] = i.getparent().getparent().findtext('ns:eventDetailInformation/ns:eventDetail',namespaces={'ns': premis_namespace})
    blank = 'n'
    print '\n**Events**\n'
    for i in all_events:

         print "%-*s   : %s" % (25,'eventType',  i.findtext('ns:eventType',namespaces={'ns': premis_namespace}))
         print "%-*s   : %s" % (25,'eventDate',  i.findtext('ns:eventDateTime',namespaces={'ns': premis_namespace}))
         print "%-*s   : %s" % (25,'eventDetail',  i.findtext('ns:eventDetailInformation/ns:eventDetail',namespaces={'ns': premis_namespace}))
         counter = 1
         for x in i.findall('ns:linkingAgentIdentifier/ns:linkingAgentIdentifierValue',namespaces={'ns': premis_namespace}):
             print "%-*s   : %s" % (25,'agentName',  agent_dict[x.text])
         print '\n'

    return event_dict

def print_agents(event_dict, input , premis, premis_namespace):
    all_agents = premis.xpath('//ns:agent',namespaces={'ns': premis_namespace})
    print '\n**Agents**\n'
    for i in all_agents:

        print "%-*s   : %s" % (25,'agentName',  i.findtext('ns:agentName',namespaces={'ns': premis_namespace}))
        print "%-*s   : %s" % (25,'agentType',  i.findtext('ns:agentType',namespaces={'ns': premis_namespace}))
        for x in i.findall('ns:linkingEventIdentifier/ns:linkingEventIdentifierValue',namespaces={'ns': premis_namespace}):
             print "%-*s   : %s" % (25,'eventName',  event_dict[x.text])
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
    print '**Summary Report **\n'
    premis_namespace    = "http://www.loc.gov/premis/v3"
    return premis, premis_namespace


def main():
    input = find_premis(sys.argv[1])
    premis, premis_namespace = create_premis_object(input)
    get_representation_info(input,premis, premis_namespace)
    agent_dict = list_agents(input,premis, premis_namespace)
    event_dict = list_events(agent_dict, input,premis, premis_namespace)
    print_agents(event_dict, input,premis, premis_namespace)


if __name__ == '__main__':
    main()



