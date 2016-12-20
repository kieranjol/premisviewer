#!/usr/bin/env python

import lxml.etree as ET
import sys
import os
import subprocess

def get_representation_info(input):
    print 'Human Readable Premis Report\n'
    parser      = ET.XMLParser(remove_blank_text=True)
    doc         = ET.parse(input,parser=parser)
    premis      = doc.getroot()
    print '**Summary Report **\n'
    premis_namespace    = "http://www.loc.gov/premis/v3"
    # some hacks in here for incorrectly formatted premis xml :((
    if premis.xpath('//ns:objectCategory',namespaces={'ns': premis_namespace})[0].text =='representation':
        representation_root =  premis.xpath('//ns:objectCategory',namespaces={'ns': premis_namespace})[0].getparent()
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


def list_agents(input):
    parser      = ET.XMLParser(remove_blank_text=True)
    doc         = ET.parse(input,parser=parser)
    premis      = doc.getroot()
    premis_namespace    = "http://www.loc.gov/premis/v3"
    all_agent_values = doc.xpath('//ns:agentIdentifierValue',namespaces={'ns': premis_namespace})
    agent_dict = {}
    for i in all_agent_values:
        agent_dict[i.text] = i.getparent().getparent().findtext('ns:agentName',namespaces={'ns': premis_namespace})
        #agent_dict[i.text] = doc.xpath(i.getparent().i.getparent() + '//ns:agentName',namespaces={'ns': premis_namespace})
    return agent_dict

def list_events(agent_dict, input):
    parser      = ET.XMLParser(remove_blank_text=True)
    doc         = ET.parse(input,parser=parser)
    premis      = doc.getroot()
    all_descendants = list(premis.iter())
    premis_namespace    = "http://www.loc.gov/premis/v3"

    all_events = doc.xpath('//ns:event',namespaces={'ns': premis_namespace})
    all_event_uuids = doc.xpath('//ns:eventIdentifierValue',namespaces={'ns': premis_namespace})
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

def print_agents(event_dict, input):
    parser      = ET.XMLParser(remove_blank_text=True)
    doc         = ET.parse(input,parser=parser)
    premis      = doc.getroot()
    premis_namespace    = "http://www.loc.gov/premis/v3"
    all_agents = doc.xpath('//ns:agent',namespaces={'ns': premis_namespace})
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


def main():
    input = find_premis(sys.argv[1])
    get_representation_info(input)
    agent_dict = list_agents(input)
    event_dict = list_events(agent_dict, input)
    print_agents(event_dict, input)


if __name__ == '__main__':
    main()



