from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Security(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	alerts: Optional[list[Alert]] = Field(default=None,alias="alerts",)
	alerts_v2: Optional[list[SecurityAlert]] = Field(default=None,alias="alerts_v2",)
	attackSimulation: Optional[AttackSimulationRoot] = Field(default=None,alias="attackSimulation",)
	cases: Optional[SecurityCasesRoot] = Field(default=None,alias="cases",)
	identities: Optional[SecurityIdentityContainer] = Field(default=None,alias="identities",)
	incidents: Optional[list[SecurityIncident]] = Field(default=None,alias="incidents",)
	labels: Optional[SecurityLabelsRoot] = Field(default=None,alias="labels",)
	secureScoreControlProfiles: Optional[list[SecureScoreControlProfile]] = Field(default=None,alias="secureScoreControlProfiles",)
	secureScores: Optional[list[SecureScore]] = Field(default=None,alias="secureScores",)
	subjectRightsRequests: Optional[list[SubjectRightsRequest]] = Field(default=None,alias="subjectRightsRequests",)
	threatIntelligence: Optional[SecurityThreatIntelligence] = Field(default=None,alias="threatIntelligence",)
	triggers: Optional[SecurityTriggersRoot] = Field(default=None,alias="triggers",)
	triggerTypes: Optional[SecurityTriggerTypesRoot] = Field(default=None,alias="triggerTypes",)

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

