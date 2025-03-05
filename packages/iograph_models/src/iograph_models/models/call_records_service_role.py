from __future__ import annotations
from enum import StrEnum


class CallRecordsServiceRole(StrEnum):
	unknown = "unknown"
	customBot = "customBot"
	skypeForBusinessMicrosoftTeamsGateway = "skypeForBusinessMicrosoftTeamsGateway"
	skypeForBusinessAudioVideoMcu = "skypeForBusinessAudioVideoMcu"
	skypeForBusinessApplicationSharingMcu = "skypeForBusinessApplicationSharingMcu"
	skypeForBusinessCallQueues = "skypeForBusinessCallQueues"
	skypeForBusinessAutoAttendant = "skypeForBusinessAutoAttendant"
	mediationServer = "mediationServer"
	mediationServerCloudConnectorEdition = "mediationServerCloudConnectorEdition"
	exchangeUnifiedMessagingService = "exchangeUnifiedMessagingService"
	mediaController = "mediaController"
	conferencingAnnouncementService = "conferencingAnnouncementService"
	conferencingAttendant = "conferencingAttendant"
	audioTeleconferencerController = "audioTeleconferencerController"
	skypeForBusinessUnifiedCommunicationApplicationPlatform = "skypeForBusinessUnifiedCommunicationApplicationPlatform"
	responseGroupServiceAnnouncementService = "responseGroupServiceAnnouncementService"
	gateway = "gateway"
	skypeTranslator = "skypeTranslator"
	skypeForBusinessAttendant = "skypeForBusinessAttendant"
	responseGroupService = "responseGroupService"
	voicemail = "voicemail"
	unknownFutureValue = "unknownFutureValue"

