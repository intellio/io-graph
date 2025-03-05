from __future__ import annotations
from enum import StrEnum


class TeamworkApplicationIdentityType(StrEnum):
	aadApplication = "aadApplication"
	bot = "bot"
	tenantBot = "tenantBot"
	office365Connector = "office365Connector"
	outgoingWebhook = "outgoingWebhook"
	unknownFutureValue = "unknownFutureValue"

