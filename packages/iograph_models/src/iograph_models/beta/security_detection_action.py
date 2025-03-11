from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDetectionAction(BaseModel):
	alertTemplate: Optional[SecurityAlertTemplate] = Field(alias="alertTemplate",default=None,)
	organizationalScope: Optional[SecurityOrganizationalScope] = Field(alias="organizationalScope",default=None,)
	responseActions: SerializeAsAny[Optional[list[SecurityResponseAction]]] = Field(alias="responseActions",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_alert_template import SecurityAlertTemplate
from .security_organizational_scope import SecurityOrganizationalScope
from .security_response_action import SecurityResponseAction

