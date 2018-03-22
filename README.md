# premisviewer

Transforms PREMIS XML into a human readable report via python/lxml
Proof of concept with much more work to be done
Usage: `premixviewer.py premis_file.xml`

A report looks like this right now - more fields to come:

```
Human Readable Premis Report

**Summary Report **

***intellectual entity***

objectIdentifierType             : UUID
objectIdentifierValue            : 15d628bd-9f66-4617-91cd-c23070184f30
objectIdentifierType             : Irish Film Archive Filmographic Database
objectIdentifierValue            : af8841

**Summary Report **

Representation includes: 1: audio/vnd.wave 43: DPX
image sequence root uuid         : 32021f82-22d3-40f1-9ce0-42ce67eeb42a
***representation***

objectIdentifierType             : UUID
objectIdentifierValue            : 4ce69e94-2e16-4e74-ac95-ab7bcd862bb2
objectIdentifierType             : Irish Film Archive Object Entry Register
objectIdentifierValue            : oe4636

***File Level***

2 formats found
Image sequence detected, only showing information about the first image object


messageDigestAlgorithm          :  md5
messageDigest                   :  f82f838dd7925cd492d4528e9abc601b
size                            :  40116874


formatName                      :  audio/vnd.wave


Count                           :  323
StreamCount                     :  1
StreamKind                      :  General
StreamKind_String               :  General
StreamKindID                    :  0
AudioCount                      :  1
Audio_Format_List               :  PCM
Audio_Format_WithHint_List      :  PCM
Audio_Codec_List                :  PCM
CompleteName                    :  af8841_ifard2016150.1_aer_lingus_people_you_know_treated.wav
FileName                        :  af8841_ifard2016150.1_aer_lingus_people_you_know_treated
FileExtension                   :  wav
Format                          :  Wave
Format_String                   :  Wave
Format_Extensions               :  wav
Format_Commercial               :  Wave
InternetMediaType               :  audio/vnd.wave
Codec                           :  Wave
Codec_String                    :  Wave
Codec_Extensions                :  wav
FileSize                        :  40116874
FileSize_String                 :  38.3 MiB
FileSize_String1                :  38 MiB
FileSize_String2                :  38 MiB
FileSize_String3                :  38.3 MiB
FileSize_String4                :  38.26 MiB
Duration                        :  69277
Duration_String                 :  1mn 9s
Duration_String1                :  1mn 9s 277ms
Duration_String2                :  1mn 9s
Duration_String3                :  00:01:09.277
Duration_String5                :  00:01:09.277
OverallBitRate_Mode             :  CBR
OverallBitRate_Mode_String      :  CBR
OverallBitRate                  :  4632634
OverallBitRate_String           :  4633 Kbps
StreamSize                      :  213010
StreamSize_String               :  208 KiB (1%)
StreamSize_String1              :  208 KiB
StreamSize_String2              :  208 KiB
StreamSize_String3              :  208 KiB
StreamSize_String4              :  208.0 KiB
StreamSize_String5              :  208 KiB (1%)
StreamSize_Proportion           :  0.00531
Producer                        :  Pro Tools
Encoded_Date                    :  2016-09-2 10:18:25
File_Modified_Date              :  UTC 2016-09-29 09:18:25
File_Modified_Date_Local        :  2016-09-29 10:18:25
Producer_Reference              :  #7XgRsTemgoaaaGk


Count                           :  272
StreamCount                     :  1
StreamKind                      :  Audio
StreamKind_String               :  Audio
StreamKindID                    :  0
Format                          :  PCM
Format_Commercial               :  PCM
Format_Settings                 :  Little / Signed
Format_Settings_Endianness      :  Little
Format_Settings_Sign            :  Signed
CodecID                         :  1
CodecID_Url                     :  http://www.microsoft.com/windows/
Codec                           :  PCM
Codec_String                    :  PCM
Codec_Family                    :  PCM
Codec_Info                      :  Microsoft PCM
Codec_Url                       :  http://www.microsoft.com/windows/
Codec_CC                        :  1
Codec_Settings                  :  Little / Signed
Codec_Settings_Endianness       :  Little
Codec_Settings_Sign             :  Signed
Duration                        :  69277
Duration_String                 :  1mn 9s
Duration_String1                :  1mn 9s 277ms
Duration_String2                :  1mn 9s
Duration_String3                :  00:01:09.277
Duration_String5                :  00:01:09.277
BitRate_Mode                    :  CBR
BitRate_Mode_String             :  CBR
BitRate                         :  4608000
BitRate_String                  :  4608 Kbps
Channel_s_                      :  2
Channel_s__String               :  2 channel2
SamplingRate                    :  96000
SamplingRate_String             :  96.0 KHz
SamplingCount                   :  6650592
Resolution                      :  24
Resolution_String               :  24 bit2
BitDepth                        :  24
BitDepth_String                 :  24 bit2
Delay                           :  1024
Delay_String                    :  1s 24ms
Delay_String1                   :  1s 24ms
Delay_String2                   :  1s 24ms
Delay_String3                   :  00:00:01.024
Delay_Source                    :  Container (bext)
Delay_Source_String             :  Container (bext)
StreamSize                      :  39903864
StreamSize_String               :  38.1 MiB (99%)
StreamSize_String1              :  38 MiB
StreamSize_String2              :  38 MiB
StreamSize_String3              :  38.1 MiB
StreamSize_String4              :  38.06 MiB
StreamSize_String5              :  38.1 MiB (99%)
StreamSize_Proportion           :  0.99469

******FIRST FILE IMAGE OBJECT DOCUMENTATION******



messageDigestAlgorithm          :  md5
messageDigest                   :  0065937e57d9dc10cbe322abb1986e25
size                            :  18876416


formatName                      :  DPX


Count                           :  322
StreamCount                     :  1
StreamKind                      :  General
StreamKind_String               :  General
StreamKindID                    :  0
ImageCount                      :  1
Image_Format_List               :  DPX
Image_Format_WithHint_List      :  DPX
CompleteName                    :  oe4636_af8841_ifard2016150.1_aer_lingus_people_you_know.0000000.dpx
FileName                        :  oe4636_af8841_ifard2016150.1_aer_lingus_people_you_know.0000000
FileExtension                   :  dpx
Format                          :  DPX
Format_String                   :  DPX
Format_Extensions               :  dpx cin
Format_Commercial               :  DPX
Format_Version                  :  Version 2.0
Codec                           :  DPX
Codec_String                    :  DPX
Codec_Extensions                :  dpx cin
FileSize                        :  18876416
FileSize_String                 :  18.0 MiB
FileSize_String1                :  18 MiB
FileSize_String2                :  18 MiB
FileSize_String3                :  18.0 MiB
FileSize_String4                :  18.00 MiB
StreamSize                      :  0
StreamSize_String               :  0.00 Byte1 (0%)
StreamSize_String1              :   Byte0
StreamSize_String2              :  0.0 Byte1
StreamSize_String3              :  0.00 Byte1
StreamSize_String4              :  0.000 Byte1
StreamSize_String5              :  0.00 Byte1 (0%)
StreamSize_Proportion           :  0.00000
Encoded_Date                    :  2016-09-30T14:51:49Z
File_Modified_Date              :  UTC 2016-09-30 14:34:54
File_Modified_Date_Local        :  2016-09-30 15:34:54
Encoded_Library                 :  AvidImageSequencer AMA Plug-in
Encoded_Library_String          :  AvidImageSequencer AMA Plug-in


Count                           :  119
StreamCount                     :  1
StreamKind                      :  Image
StreamKind_String               :  Image
StreamKindID                    :  0
Format                          :  DPX
Format_Commercial               :  DPX
Format_Version                  :  Version 2.0
Width                           :  2048
Width_String                    :  2048 pixel3
Height                          :  1536
Height_String                   :  1536 pixel3
PixelAspectRatio                :  1.000
DisplayAspectRatio              :  1.333
DisplayAspectRatio_String       :  4:3
ColorSpace                      :  RGB
Resolution                      :  12
Resolution_String               :  12 bit3
BitDepth                        :  12
BitDepth_String                 :  12 bit3
Compression_Mode                :  Lossless
Compression_Mode_String         :  Lossless
StreamSize                      :  18876416
StreamSize_String               :  18.0 MiB (100%)
StreamSize_String1              :  18 MiB
StreamSize_String2              :  18 MiB
StreamSize_String3              :  18.0 MiB
StreamSize_String4              :  18.00 MiB
StreamSize_String5              :  18.0 MiB (100%)
StreamSize_Proportion           :  1.00000
Encoded_Library                 :  AvidImageSequencer AMA Plug-in
Encoded_Library_String          :  AvidImageSequencer AMA Plug-in
Encoded_Date                    :  2016-09-30T14:51:49Z
colour_description_present      :  Yes
FrameRate                       :  24.000

******END OF FIRST FILE IMAGE OBJECT DOCUMENTATION******


**Events**

eventType                        : creation
eventDate                        : 2016-09-29T10:18:25
eventDetail                      : Audio cleanup
agentName                        : mac mini
agentName                        : osx
agentName                        : iZotope Rx5
agentName                        : Brian Cash


eventType                        : creation
eventDate                        : 2016-09-29T10:18:25
eventDetail                      : Audio trimming and export
agentName                        : mac mini
agentName                        : osx
agentName                        : ProTools
agentName                        : Brian Cash


eventType                        : creation
eventDate                        : 2016-09-30T15:34:54
eventDetail                      : Import to Avid and remove overscan
agentName                        : Mac Pro
agentName                        : osx
agentName                        : Avid Media Composer
agentName                        : Gavin Martin


eventType                        : creation
eventDate                        : 2016-09-30T15:34:54
eventDetail                      : Colour Correction
agentName                        : Mac Pro
agentName                        : osx
agentName                        : Baselight
agentName                        : Gavin Martin


eventType                        : message digest calculation
eventDate                        : 2017-01-05T11:14:35
eventDetail                      : Frame level checksums of image
agentName                        : mac mini
agentName                        : osx
agentName                        : ffmpeg
agentName                        : Gavin Martin


eventType                        : message digest calculation
eventDate                        : 2017-01-05T11:14:35
eventDetail                      : Checksum manifest for whole package created
agentName                        : hashlib
agentName                        : mac mini
agentName                        : osx
agentName                        : Gavin Martin



**Agents**

agentName                        : Gavin Martin
agentType                        : person
eventName                        : Import to Avid and remove overscan
eventName                        : Colour Correction
eventName                        : Checksum manifest for whole package created
eventName                        : Frame level checksums of image


agentName                        : Brian Cash
agentType                        : person
eventName                        : Audio cleanup
eventName                        : Audio trimming and export


agentName                        : mac mini
agentType                        : hardware
eventName                        : Audio cleanup
eventName                        : Checksum manifest for whole package created
eventName                        : Frame level checksums of image
eventName                        : Audio trimming and export


agentName                        : Mac Pro
agentType                        : hardware
eventName                        : Audio cleanup
eventName                        : Checksum manifest for whole package created
eventName                        : Audio trimming and export
eventName                        : Frame level checksums of image


agentName                        : osx
agentType                        : software
eventName                        : Audio cleanup
eventName                        : Checksum manifest for whole package created
eventName                        : Audio trimming and export
eventName                        : Frame level checksums of image


agentName                        : osx
agentType                        : software
eventName                        : Import to Avid and remove overscan
eventName                        : Colour Correction


agentName                        : ffmpeg
agentType                        : software
eventName                        : Frame level checksums of image


agentName                        : hashlib
agentType                        : software
eventName                        : Checksum manifest for whole package created


agentName                        : Avid Media Composer
agentType                        : software
eventName                        : Import to Avid and remove overscan
eventName                        : Colour Correction


agentName                        : ProTools
agentType                        : software
eventName                        : Audio trimming and export


agentName                        : Baselight
agentType                        : software
eventName                        : Colour Correction


agentName                        : iZotope Rx5
agentType                        : software
eventName                        : Audio cleanup
```
