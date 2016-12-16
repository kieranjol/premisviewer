#!/usr/bin/env python
import lxml.etree as ET
import sys
import os
import subprocess

def get_representation_info():
    print 'Human Readable Premis Report\n'
    parser      = ET.XMLParser(remove_blank_text=True)
    doc         = ET.parse(sys.argv[1],parser=parser)
    premis      = doc.getroot()
    print '**Representation Level **\n'
    premis_namespace    = "http://www.loc.gov/premis/v3"
    # some hacks in here for incorrectly formatted premis xml :((
    if premis.xpath('//ns:objectCategory',namespaces={'ns': premis_namespace})[0].text =='representation':
        representation_root =  premis.xpath('//ns:objectCategory',namespaces={'ns': premis_namespace})[0].getparent()
        if representation_root.xpath('//ns:relationshipSubType',namespaces={'ns': premis_namespace})[0].text == 'has source':
            source_relationship_root = representation_root.xpath('//ns:relationshipSubType',namespaces={'ns': premis_namespace})[0].getparent()
            source_id =  source_relationship_root.findtext('ns:relatedObjectIdentifier/ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
            if source_id == None:
                source_id =  source_relationship_root.findtext('ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
            print " %-*s   %s" % (25,'has source', source_id)
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
        #commenting as this code was based on an audio track having the only 'includes' relationship, the images had 'has root'
        
        inputs  = ['%s: %s' % (v, k) for k, v in format_dict.items()]
        print 'Representation includes:', ' '.join(inputs)

        
        '''''
        for i in included_files:
            
            
            included_file_uuid = i.findtext('ns:relatedObjectIdentifier/ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
            if included_file_uuid == None:
                included_file_uuid = i.findtext('ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
            print " %-*s   %s" % (25,'included file uuid',included_file_uuid)
            included_format =  premis.xpath("//ns:formatName[../../../..//ns:objectIdentifierValue='%s' ]" % included_file_uuid ,namespaces={'ns': premis_namespace})
            
            print " %-*s   %s" % (25,'includes', included_format[0].text)  
        ''' 
        image_sequence_uuid = representation_root.xpath("ns:relationship[ns:relationshipSubType='has root']",namespaces={'ns': premis_namespace})
        if len(image_sequence_uuid) > 0:
            if not image_sequence_uuid[0] in ['', None]:
                root_uuid = image_sequence_uuid[0].findtext('ns:relatedObjectIdentifier/ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
                if root_uuid == None:
                    root_uuid = image_sequence_uuid[0].findtext('ns:relatedObjectIdentifierValue',namespaces={'ns': premis_namespace})
                print "%-*s   %s" % (25,'image sequence root uuid',root_uuid)
                file_format =  premis.xpath("//ns:formatName[../../../..//ns:objectIdentifierValue='%s' ]" % root_uuid,namespaces={'ns': premis_namespace})
                image_count =  len(premis.xpath("//ns:formatDesignation[ns:formatName='%s' ]" % file_format[0].text,namespaces={'ns': premis_namespace}))
                
                print "%-*s   %s" % (25,'image sequence format', file_format[0].text) 
                #print 'Representation contains : %s %s files and %s %s' % (image_count, file_format[0].text, included_count, included_format[0].text )
        
    '''''
    agent_dict = {}
    for i in all_agent_values:
        agent_dict[i.text] = i.getparent().getparent().findtext('ns:agentName',namespaces={'ns': premis_namespace})
        #agent_dict[i.text] = doc.xpath(i.getparent().i.getparent() + '//ns:agentName',namespaces={'ns': premis_namespace})
    return agent_dict
    '''   

def list_agents():
    parser      = ET.XMLParser(remove_blank_text=True)
    doc         = ET.parse(sys.argv[1],parser=parser)
    premis      = doc.getroot()
    premis_namespace    = "http://www.loc.gov/premis/v3"
    all_agent_values = doc.xpath('//ns:agentIdentifierValue',namespaces={'ns': premis_namespace})
    agent_dict = {}
    for i in all_agent_values:
        agent_dict[i.text] = i.getparent().getparent().findtext('ns:agentName',namespaces={'ns': premis_namespace})
        #agent_dict[i.text] = doc.xpath(i.getparent().i.getparent() + '//ns:agentName',namespaces={'ns': premis_namespace})
    return agent_dict
       
def list_events(agent_dict):
    parser      = ET.XMLParser(remove_blank_text=True)
    doc         = ET.parse(sys.argv[1],parser=parser)
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
         
         print " %-*s   %s" % (25,'eventType',  i.findtext('ns:eventType',namespaces={'ns': premis_namespace}))
         print " %-*s   %s" % (25,'eventDate',  i.findtext('ns:eventDateTime',namespaces={'ns': premis_namespace}))
         print " %-*s   %s" % (25,'eventDetail',  i.findtext('ns:eventDetailInformation/ns:eventDetail',namespaces={'ns': premis_namespace}))
         counter = 1
         for x in i.findall('ns:linkingAgentIdentifier/ns:linkingAgentIdentifierValue',namespaces={'ns': premis_namespace}):
             print " %-*s   %s" % (25,'agentName',  agent_dict[x.text])
         print '\n'

    return event_dict 

def print_agents(event_dict):
    parser      = ET.XMLParser(remove_blank_text=True)
    doc         = ET.parse(sys.argv[1],parser=parser)
    premis      = doc.getroot()
    premis_namespace    = "http://www.loc.gov/premis/v3"
    all_agents = doc.xpath('//ns:agent',namespaces={'ns': premis_namespace})
    print '\n**Agents**\n'
    for i in all_agents:

            print " %-*s   %s" % (25,'agentName',  i.findtext('ns:agentName',namespaces={'ns': premis_namespace}))
            print " %-*s   %s" % (25,'agentType',  i.findtext('ns:agentType',namespaces={'ns': premis_namespace}))
            
            for x in i.findall('ns:linkingEventIdentifier/ns:linkingEventIdentifierValue',namespaces={'ns': premis_namespace}):
                 print " %-*s   %s" % (25,'eventName',  event_dict[x.text])
            print '\n'
                    
def main():
    
    parser      = ET.XMLParser(remove_blank_text=True)
    doc         = ET.parse(sys.argv[1],parser=parser)
    premis      = doc.getroot()
    all_descendants = list(premis.iter())
    blank = 'n'
    for i in all_descendants:
         
         if i.text == None:
             if blank == 'n':
                print '\n'
                blank = 'y'
         else:
                blank = 'n'
                print " %-*s   %s" % (50,i.tag.replace('{http://www.loc.gov/premis/v3}',''),  i.text)
if __name__ == '__main__':
    
    get_representation_info()
    agent_dict = list_agents()
    event_dict = list_events(agent_dict)
    print_agents(event_dict) 
    
    
