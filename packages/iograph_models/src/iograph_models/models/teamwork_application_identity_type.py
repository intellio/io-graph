from __future__ import annotations
from enum import Enum


class TeamworkApplicationIdentityType(Enum):
	aadApplication = "aadApplication"
	bot = "bot"
	tenantBot = "tenantBot"
	office365Connector = "office365Connector"
	outgoingWebhook = "outgoingWebhook"
	unknownFutureValue = "unknownFutureValue"

