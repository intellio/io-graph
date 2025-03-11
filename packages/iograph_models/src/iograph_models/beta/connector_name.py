from __future__ import annotations
from enum import StrEnum


class ConnectorName(StrEnum):
	applePushNotificationServiceExpirationDateTime = "applePushNotificationServiceExpirationDateTime"
	vppTokenExpirationDateTime = "vppTokenExpirationDateTime"
	vppTokenLastSyncDateTime = "vppTokenLastSyncDateTime"
	windowsAutopilotLastSyncDateTime = "windowsAutopilotLastSyncDateTime"
	windowsStoreForBusinessLastSyncDateTime = "windowsStoreForBusinessLastSyncDateTime"
	jamfLastSyncDateTime = "jamfLastSyncDateTime"
	ndesConnectorLastConnectionDateTime = "ndesConnectorLastConnectionDateTime"
	appleDepExpirationDateTime = "appleDepExpirationDateTime"
	appleDepLastSyncDateTime = "appleDepLastSyncDateTime"
	onPremConnectorLastSyncDateTime = "onPremConnectorLastSyncDateTime"
	googlePlayAppLastSyncDateTime = "googlePlayAppLastSyncDateTime"
	googlePlayConnectorLastModifiedDateTime = "googlePlayConnectorLastModifiedDateTime"
	windowsDefenderATPConnectorLastHeartbeatDateTime = "windowsDefenderATPConnectorLastHeartbeatDateTime"
	mobileThreatDefenceConnectorLastHeartbeatDateTime = "mobileThreatDefenceConnectorLastHeartbeatDateTime"
	chromebookLastDirectorySyncDateTime = "chromebookLastDirectorySyncDateTime"
	futureValue = "futureValue"

