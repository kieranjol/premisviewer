# premisviewer
Transforms PREMIS XML into a human readable report via python/lxml
Proof of concept with much more work to be done
Usage: `premixviewer.py premis_file.xml`

A report looks like this right now - more fields to come:

**Summary Report **

***intellectual entity***

objectIdentifierType        : None
objectIdentifierValue       : None
objectIdentifierType        : UUID
objectIdentifierValue       : d6ad2534-b5f0-40c9-aa9f-5ae2cfcdfc35
objectIdentifierType        : Irish Film Archive Filmographic Database
objectIdentifierValue       : af8841
Human Readable Premis Report

**Summary Report **

Representation includes: 1: audio/vnd.wave 43: DPX
image sequence root uuid    : 8f5b7490-9225-4855-99aa-1fb61472d896
***representation***

objectIdentifierType        : UUID
objectIdentifierValue       : 3c92e9d2-2e1b-4dec-8fcb-8ed21f236306
objectIdentifierType        : Irish Film Archive Object Entry Register
objectIdentifierValue       : oe4636

**Events**

eventType                   : creation
eventDate                   : 2016-09-29T10:18:25
eventDetail                 : Audio cleanup
agentName                   : mac mini
agentName                   : osx
agentName                   : iZotope Rx5
agentName                   : Brian Cash


eventType                   : creation
eventDate                   : 2016-09-29T10:18:25
eventDetail                 : Audio trimming and export
agentName                   : mac mini
agentName                   : osx
agentName                   : ProTools
agentName                   : Brian Cash


eventType                   : creation
eventDate                   : 2016-09-30T15:34:54
eventDetail                 : Import to Avid and remove overscan
agentName                   : Mac Pro
agentName                   : osx
agentName                   : Avid Media Composer
agentName                   : Gavin Martin


eventType                   : creation
eventDate                   : 2016-09-30T15:34:54
eventDetail                 : Colour Correction
agentName                   : Mac Pro
agentName                   : osx
agentName                   : Baselight
agentName                   : Gavin Martin


eventType                   : message digest calculation
eventDate                   : 2017-01-04T13:00:20
eventDetail                 : Frame level checksums of image
agentName                   : mac mini
agentName                   : osx
agentName                   : ffmpeg
agentName                   : Kieran O'Leary


eventType                   : message digest calculation
eventDate                   : 2017-01-04T13:00:20
eventDetail                 : Checksum manifest for whole package created
agentName                   : hashlib
agentName                   : mac mini
agentName                   : osx
agentName                   : Kieran O'Leary



**Agents**

agentName                   : Kieran O'Leary
agentType                   : person
eventName                   : Checksum manifest for whole package created
eventName                   : Frame level checksums of image


agentName                   : Gavin Martin
agentType                   : person
eventName                   : Import to Avid and remove overscan
eventName                   : Colour Correction


agentName                   : Brian Cash
agentType                   : person
eventName                   : Audio cleanup
eventName                   : Audio trimming and export


agentName                   : mac mini
agentType                   : hardware
eventName                   : Audio cleanup
eventName                   : Checksum manifest for whole package created
eventName                   : Frame level checksums of image
eventName                   : Audio trimming and export


agentName                   : Mac Pro
agentType                   : hardware
eventName                   : Audio cleanup
eventName                   : Checksum manifest for whole package created
eventName                   : Audio trimming and export
eventName                   : Frame level checksums of image


agentName                   : osx
agentType                   : software
eventName                   : Audio cleanup
eventName                   : Checksum manifest for whole package created
eventName                   : Audio trimming and export
eventName                   : Frame level checksums of image


agentName                   : osx
agentType                   : software
eventName                   : Import to Avid and remove overscan
eventName                   : Colour Correction


agentName                   : ffmpeg
agentType                   : software
eventName                   : Frame level checksums of image


agentName                   : hashlib
agentType                   : software
eventName                   : Checksum manifest for whole package created


agentName                   : Avid Media Composer
agentType                   : software
eventName                   : Import to Avid and remove overscan
eventName                   : Colour Correction


agentName                   : ProTools
agentType                   : software
eventName                   : Audio trimming and export


agentName                   : Baselight
agentType                   : software
eventName                   : Colour Correction


agentName                   : iZotope Rx5
agentType                   : software
eventName                   : Audio cleanup