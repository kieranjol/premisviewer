# premisviewer
Transforms PREMIS XML into a human readable report via python/lxml
Proof of concept with much more work to be done
Usage: `premixviewer.py premis_file.xml`

A report looks like this right now - more fields to come:

Human Readable Premis Report

**Representation Level **

Representation includes: 1: audio/vnd.wave 403: DPX
image sequence root uuid    cfec5e83-77ff-4c2a-8518-42e40f59b981
image sequence format       DPX

**Events**

 eventType                   creation
 eventDate                   2016-12-15T16:19:21
 eventDetail                 Audio cleanup
 agentName                   mac mini
 agentName                   osx
 agentName                   iZotope Rx5
 agentName                   Brian Cash


 eventType                   creation
 eventDate                   2016-12-15T16:19:21
 eventDetail                 Audio trimming and export
 agentName                   mac mini
 agentName                   osx
 agentName                   ProTools
 agentName                   Brian Cash


 eventType                   creation
 eventDate                   2016-12-15T16:19:21
 eventDetail                 Import to Avid and remove overscan
 agentName                   Mac Pro
 agentName                   osx
 agentName                   Avid Media Composer
 agentName                   Gavin Martin


 eventType                   creation
 eventDate                   2016-12-15T16:19:21
 eventDetail                 Colour Correction
 agentName                   Mac Pro
 agentName                   osx
 agentName                   Baselight
 agentName                   Gavin Martin


 eventType                   message digest calculation
 eventDate                   2016-12-15T16:19:21
 eventDetail                 Frame level checksums of image
 agentName                   mac mini
 agentName                   osx
 agentName                   ffmpeg
 agentName                   Raelene Casey


 eventType                   message digest calculation
 eventDate                   2016-12-15T16:19:21
 eventDetail                 Checksum manifest for whole package created
 agentName                   hashlib
 agentName                   mac mini
 agentName                   osx
 agentName                   Raelene Casey



**Agents**

 agentName                   Raelene Casey
 agentType                   person
 eventName                   Checksum manifest for whole package created
 eventName                   Frame level checksums of image


 agentName                   Gavin Martin
 agentType                   person
 eventName                   Import to Avid and remove overscan
 eventName                   Colour Correction


 agentName                   Brian Cash
 agentType                   person
 eventName                   Audio cleanup
 eventName                   Audio trimming and export


 agentName                   mac mini
 agentType                   hardware
 eventName                   Audio cleanup
 eventName                   Checksum manifest for whole package created
 eventName                   Frame level checksums of image
 eventName                   Audio trimming and export


 agentName                   Mac Pro
 agentType                   hardware
 eventName                   Audio cleanup
 eventName                   Checksum manifest for whole package created
 eventName                   Audio trimming and export
 eventName                   Frame level checksums of image


 agentName                   osx
 agentType                   software
 eventName                   Audio cleanup
 eventName                   Checksum manifest for whole package created
 eventName                   Audio trimming and export
 eventName                   Frame level checksums of image


 agentName                   osx
 agentType                   software
 eventName                   Import to Avid and remove overscan
 eventName                   Colour Correction


 agentName                   ffmpeg
 agentType                   software
 eventName                   Frame level checksums of image


 agentName                   hashlib
 agentType                   software
 eventName                   Checksum manifest for whole package created


 agentName                   Avid Media Composer
 agentType                   software
 eventName                   Import to Avid and remove overscan
 eventName                   Colour Correction


 agentName                   ProTools
 agentType                   software
 eventName                   Audio trimming and export


 agentName                   Baselight
 agentType                   software
 eventName                   Colour Correction


 agentName                   iZotope Rx5
 agentType                   software
 eventName                   Audio cleanup
