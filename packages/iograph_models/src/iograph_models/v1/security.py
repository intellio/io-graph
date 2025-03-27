from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	alerts: Optional[list[Alert]] = Field(alias="alerts", default=None,)
	alerts_v2: Optional[list[SecurityAlert]] = Field(alias="alerts_v2", default=None,)
	attackSimulation: Optional[AttackSimulationRoot] = Field(alias="attackSimulation", default=None,)
	cases: Optional[SecurityCasesRoot] = Field(alias="cases", default=None,)
	identities: Optional[SecurityIdentityContainer] = Field(alias="identities", default=None,)
	incidents: Optional[list[SecurityIncident]] = Field(alias="incidents", default=None,)
	labels: Optional[SecurityLabelsRoot] = Field(alias="labels", default=None,)
	secureScoreControlProfiles: Optional[list[SecureScoreControlProfile]] = Field(alias="secureScoreControlProfiles", default=None,)
	secureScores: Optional[list[SecureScore]] = Field(alias="secureScores", default=None,)
	subjectRightsRequests: Optional[list[SubjectRightsRequest]] = Field(alias="subjectRightsRequests", default=None,)
	threatIntelligence: Optional[SecurityThreatIntelligence] = Field(alias="threatIntelligence", default=None,)
	triggers: Optional[SecurityTriggersRoot] = Field(alias="triggers", default=None,)
	triggerTypes: Optional[SecurityTriggerTypesRoot] = Field(alias="triggerTypes", default=None,)

from .alert import Alert
from .security_alert import SecurityAlert
from .attack_simulation_root import AttackSimulationRoot
from .security_cases_root import SecurityCasesRoot
from .security_identity_container import SecurityIdentityContainer
from .security_incident import SecurityIncident
from .security_labels_root import SecurityLabelsRoot
from .secure_score_control_profile import SecureScoreControlProfile
from .secure_score import SecureScore
from .subject_rights_request import SubjectRightsRequest
from .security_threat_intelligence import SecurityThreatIntelligence
from .security_triggers_root import SecurityTriggersRoot
from .security_trigger_types_root import SecurityTriggerTypesRoot

