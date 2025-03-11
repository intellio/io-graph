from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security(BaseModel):
	alerts: Optional[list[Alert]] = Field(alias="alerts",default=None,)
	alerts_v2: Optional[list[SecurityAlert]] = Field(alias="alerts_v2",default=None,)
	attackSimulation: Optional[AttackSimulationRoot] = Field(alias="attackSimulation",default=None,)
	auditLog: Optional[SecurityAuditCoreRoot] = Field(alias="auditLog",default=None,)
	cases: Optional[SecurityCasesRoot] = Field(alias="cases",default=None,)
	cloudAppSecurityProfiles: Optional[list[CloudAppSecurityProfile]] = Field(alias="cloudAppSecurityProfiles",default=None,)
	collaboration: Optional[SecurityCollaborationRoot] = Field(alias="collaboration",default=None,)
	dataDiscovery: Optional[SecurityDataDiscoveryRoot] = Field(alias="dataDiscovery",default=None,)
	domainSecurityProfiles: Optional[list[DomainSecurityProfile]] = Field(alias="domainSecurityProfiles",default=None,)
	fileSecurityProfiles: Optional[list[FileSecurityProfile]] = Field(alias="fileSecurityProfiles",default=None,)
	hostSecurityProfiles: Optional[list[HostSecurityProfile]] = Field(alias="hostSecurityProfiles",default=None,)
	identities: Optional[SecurityIdentityContainer] = Field(alias="identities",default=None,)
	incidents: Optional[list[SecurityIncident]] = Field(alias="incidents",default=None,)
	informationProtection: Optional[SecurityInformationProtection] = Field(alias="informationProtection",default=None,)
	ipSecurityProfiles: Optional[list[IpSecurityProfile]] = Field(alias="ipSecurityProfiles",default=None,)
	labels: Optional[SecurityLabelsRoot] = Field(alias="labels",default=None,)
	partner: Optional[PartnerSecurityPartnerSecurity] = Field(alias="partner",default=None,)
	providerTenantSettings: Optional[list[ProviderTenantSetting]] = Field(alias="providerTenantSettings",default=None,)
	rules: Optional[SecurityRulesRoot] = Field(alias="rules",default=None,)
	secureScoreControlProfiles: Optional[list[SecureScoreControlProfile]] = Field(alias="secureScoreControlProfiles",default=None,)
	secureScores: Optional[list[SecureScore]] = Field(alias="secureScores",default=None,)
	securityActions: Optional[list[SecurityAction]] = Field(alias="securityActions",default=None,)
	subjectRightsRequests: Optional[list[SubjectRightsRequest]] = Field(alias="subjectRightsRequests",default=None,)
	threatIntelligence: Optional[SecurityThreatIntelligence] = Field(alias="threatIntelligence",default=None,)
	threatSubmission: Optional[SecurityThreatSubmissionRoot] = Field(alias="threatSubmission",default=None,)
	tiIndicators: Optional[list[TiIndicator]] = Field(alias="tiIndicators",default=None,)
	triggers: Optional[SecurityTriggersRoot] = Field(alias="triggers",default=None,)
	triggerTypes: Optional[SecurityTriggerTypesRoot] = Field(alias="triggerTypes",default=None,)
	userSecurityProfiles: Optional[list[UserSecurityProfile]] = Field(alias="userSecurityProfiles",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .alert import Alert
from .security_alert import SecurityAlert
from .attack_simulation_root import AttackSimulationRoot
from .security_audit_core_root import SecurityAuditCoreRoot
from .security_cases_root import SecurityCasesRoot
from .cloud_app_security_profile import CloudAppSecurityProfile
from .security_collaboration_root import SecurityCollaborationRoot
from .security_data_discovery_root import SecurityDataDiscoveryRoot
from .domain_security_profile import DomainSecurityProfile
from .file_security_profile import FileSecurityProfile
from .host_security_profile import HostSecurityProfile
from .security_identity_container import SecurityIdentityContainer
from .security_incident import SecurityIncident
from .security_information_protection import SecurityInformationProtection
from .ip_security_profile import IpSecurityProfile
from .security_labels_root import SecurityLabelsRoot
from .partner_security_partner_security import PartnerSecurityPartnerSecurity
from .provider_tenant_setting import ProviderTenantSetting
from .security_rules_root import SecurityRulesRoot
from .secure_score_control_profile import SecureScoreControlProfile
from .secure_score import SecureScore
from .security_action import SecurityAction
from .subject_rights_request import SubjectRightsRequest
from .security_threat_intelligence import SecurityThreatIntelligence
from .security_threat_submission_root import SecurityThreatSubmissionRoot
from .ti_indicator import TiIndicator
from .security_triggers_root import SecurityTriggersRoot
from .security_trigger_types_root import SecurityTriggerTypesRoot
from .user_security_profile import UserSecurityProfile

