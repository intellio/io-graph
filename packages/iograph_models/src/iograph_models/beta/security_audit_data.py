from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class SecurityAuditData(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.security.aadRiskDetectionAuditRecord":
				from .security_aad_risk_detection_audit_record import SecurityAadRiskDetectionAuditRecord
				return SecurityAadRiskDetectionAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.aedAuditRecord":
				from .security_aed_audit_record import SecurityAedAuditRecord
				return SecurityAedAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.aiAppInteractionAuditRecord":
				from .security_ai_app_interaction_audit_record import SecurityAiAppInteractionAuditRecord
				return SecurityAiAppInteractionAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.aipFileDeleted":
				from .security_aip_file_deleted import SecurityAipFileDeleted
				return SecurityAipFileDeleted.model_validate(data)
			if mapping_key == "#microsoft.graph.security.aipHeartBeat":
				from .security_aip_heart_beat import SecurityAipHeartBeat
				return SecurityAipHeartBeat.model_validate(data)
			if mapping_key == "#microsoft.graph.security.aipProtectionActionLogRequest":
				from .security_aip_protection_action_log_request import SecurityAipProtectionActionLogRequest
				return SecurityAipProtectionActionLogRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.security.aipScannerDiscoverEvent":
				from .security_aip_scanner_discover_event import SecurityAipScannerDiscoverEvent
				return SecurityAipScannerDiscoverEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.security.aipSensitivityLabelActionLogRequest":
				from .security_aip_sensitivity_label_action_log_request import SecurityAipSensitivityLabelActionLogRequest
				return SecurityAipSensitivityLabelActionLogRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.security.airAdminActionInvestigationData":
				from .security_air_admin_action_investigation_data import SecurityAirAdminActionInvestigationData
				return SecurityAirAdminActionInvestigationData.model_validate(data)
			if mapping_key == "#microsoft.graph.security.airInvestigationData":
				from .security_air_investigation_data import SecurityAirInvestigationData
				return SecurityAirInvestigationData.model_validate(data)
			if mapping_key == "#microsoft.graph.security.airManualInvestigationData":
				from .security_air_manual_investigation_data import SecurityAirManualInvestigationData
				return SecurityAirManualInvestigationData.model_validate(data)
			if mapping_key == "#microsoft.graph.security.attackSimAdminAuditRecord":
				from .security_attack_sim_admin_audit_record import SecurityAttackSimAdminAuditRecord
				return SecurityAttackSimAdminAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.auditSearchAuditRecord":
				from .security_audit_search_audit_record import SecurityAuditSearchAuditRecord
				return SecurityAuditSearchAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.azureActiveDirectoryAccountLogonAuditRecord":
				from .security_azure_active_directory_account_logon_audit_record import SecurityAzureActiveDirectoryAccountLogonAuditRecord
				return SecurityAzureActiveDirectoryAccountLogonAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.azureActiveDirectoryAuditRecord":
				from .security_azure_active_directory_audit_record import SecurityAzureActiveDirectoryAuditRecord
				return SecurityAzureActiveDirectoryAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.azureActiveDirectoryBaseAuditRecord":
				from .security_azure_active_directory_base_audit_record import SecurityAzureActiveDirectoryBaseAuditRecord
				return SecurityAzureActiveDirectoryBaseAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.azureActiveDirectoryStsLogonAuditRecord":
				from .security_azure_active_directory_sts_logon_audit_record import SecurityAzureActiveDirectoryStsLogonAuditRecord
				return SecurityAzureActiveDirectoryStsLogonAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.campaignAuditRecord":
				from .security_campaign_audit_record import SecurityCampaignAuditRecord
				return SecurityCampaignAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.caseAuditRecord":
				from .security_case_audit_record import SecurityCaseAuditRecord
				return SecurityCaseAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.caseInvestigation":
				from .security_case_investigation import SecurityCaseInvestigation
				return SecurityCaseInvestigation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cdpColdCrawlStatusRecord":
				from .security_cdp_cold_crawl_status_record import SecurityCdpColdCrawlStatusRecord
				return SecurityCdpColdCrawlStatusRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cdpContentExplorerAggregateRecord":
				from .security_cdp_content_explorer_aggregate_record import SecurityCdpContentExplorerAggregateRecord
				return SecurityCdpContentExplorerAggregateRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cdpDlpSensitiveAuditRecord":
				from .security_cdp_dlp_sensitive_audit_record import SecurityCdpDlpSensitiveAuditRecord
				return SecurityCdpDlpSensitiveAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cdpDlpSensitiveEndpointAuditRecord":
				from .security_cdp_dlp_sensitive_endpoint_audit_record import SecurityCdpDlpSensitiveEndpointAuditRecord
				return SecurityCdpDlpSensitiveEndpointAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cdpLogRecord":
				from .security_cdp_log_record import SecurityCdpLogRecord
				return SecurityCdpLogRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cdpOcrBillingRecord":
				from .security_cdp_ocr_billing_record import SecurityCdpOcrBillingRecord
				return SecurityCdpOcrBillingRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cdpResourceScopeChangeEventRecord":
				from .security_cdp_resource_scope_change_event_record import SecurityCdpResourceScopeChangeEventRecord
				return SecurityCdpResourceScopeChangeEventRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cernerSMSLinkRecord":
				from .security_cerner_s_m_s_link_record import SecurityCernerSMSLinkRecord
				return SecurityCernerSMSLinkRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cernerSMSSettingsUpdateRecord":
				from .security_cerner_s_m_s_settings_update_record import SecurityCernerSMSSettingsUpdateRecord
				return SecurityCernerSMSSettingsUpdateRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cernerSMSUnlinkRecord":
				from .security_cerner_s_m_s_unlink_record import SecurityCernerSMSUnlinkRecord
				return SecurityCernerSMSUnlinkRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceConnectorAuditRecord":
				from .security_compliance_connector_audit_record import SecurityComplianceConnectorAuditRecord
				return SecurityComplianceConnectorAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDLMExchangeAuditRecord":
				from .security_compliance_d_l_m_exchange_audit_record import SecurityComplianceDLMExchangeAuditRecord
				return SecurityComplianceDLMExchangeAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDLMSharePointAuditRecord":
				from .security_compliance_d_l_m_share_point_audit_record import SecurityComplianceDLMSharePointAuditRecord
				return SecurityComplianceDLMSharePointAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpApplicationsAuditRecord":
				from .security_compliance_dlp_applications_audit_record import SecurityComplianceDlpApplicationsAuditRecord
				return SecurityComplianceDlpApplicationsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpApplicationsClassificationAuditRecord":
				from .security_compliance_dlp_applications_classification_audit_record import SecurityComplianceDlpApplicationsClassificationAuditRecord
				return SecurityComplianceDlpApplicationsClassificationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpBaseAuditRecord":
				from .security_compliance_dlp_base_audit_record import SecurityComplianceDlpBaseAuditRecord
				return SecurityComplianceDlpBaseAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpClassificationBaseAuditRecord":
				from .security_compliance_dlp_classification_base_audit_record import SecurityComplianceDlpClassificationBaseAuditRecord
				return SecurityComplianceDlpClassificationBaseAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpClassificationBaseCdpRecord":
				from .security_compliance_dlp_classification_base_cdp_record import SecurityComplianceDlpClassificationBaseCdpRecord
				return SecurityComplianceDlpClassificationBaseCdpRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpEndpointAuditRecord":
				from .security_compliance_dlp_endpoint_audit_record import SecurityComplianceDlpEndpointAuditRecord
				return SecurityComplianceDlpEndpointAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpEndpointDiscoveryAuditRecord":
				from .security_compliance_dlp_endpoint_discovery_audit_record import SecurityComplianceDlpEndpointDiscoveryAuditRecord
				return SecurityComplianceDlpEndpointDiscoveryAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpExchangeAuditRecord":
				from .security_compliance_dlp_exchange_audit_record import SecurityComplianceDlpExchangeAuditRecord
				return SecurityComplianceDlpExchangeAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpExchangeClassificationAuditRecord":
				from .security_compliance_dlp_exchange_classification_audit_record import SecurityComplianceDlpExchangeClassificationAuditRecord
				return SecurityComplianceDlpExchangeClassificationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpExchangeClassificationCdpRecord":
				from .security_compliance_dlp_exchange_classification_cdp_record import SecurityComplianceDlpExchangeClassificationCdpRecord
				return SecurityComplianceDlpExchangeClassificationCdpRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpExchangeDiscoveryAuditRecord":
				from .security_compliance_dlp_exchange_discovery_audit_record import SecurityComplianceDlpExchangeDiscoveryAuditRecord
				return SecurityComplianceDlpExchangeDiscoveryAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpSharePointAuditRecord":
				from .security_compliance_dlp_share_point_audit_record import SecurityComplianceDlpSharePointAuditRecord
				return SecurityComplianceDlpSharePointAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpSharePointClassificationAuditRecord":
				from .security_compliance_dlp_share_point_classification_audit_record import SecurityComplianceDlpSharePointClassificationAuditRecord
				return SecurityComplianceDlpSharePointClassificationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceDlpSharePointClassificationExtendedAuditRecord":
				from .security_compliance_dlp_share_point_classification_extended_audit_record import SecurityComplianceDlpSharePointClassificationExtendedAuditRecord
				return SecurityComplianceDlpSharePointClassificationExtendedAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceManagerActionRecord":
				from .security_compliance_manager_action_record import SecurityComplianceManagerActionRecord
				return SecurityComplianceManagerActionRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceSupervisionBaseAuditRecord":
				from .security_compliance_supervision_base_audit_record import SecurityComplianceSupervisionBaseAuditRecord
				return SecurityComplianceSupervisionBaseAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.complianceSupervisionExchangeAuditRecord":
				from .security_compliance_supervision_exchange_audit_record import SecurityComplianceSupervisionExchangeAuditRecord
				return SecurityComplianceSupervisionExchangeAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.consumptionResourceAuditRecord":
				from .security_consumption_resource_audit_record import SecurityConsumptionResourceAuditRecord
				return SecurityConsumptionResourceAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.copilotInteractionAuditRecord":
				from .security_copilot_interaction_audit_record import SecurityCopilotInteractionAuditRecord
				return SecurityCopilotInteractionAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.coreReportingSettingsAuditRecord":
				from .security_core_reporting_settings_audit_record import SecurityCoreReportingSettingsAuditRecord
				return SecurityCoreReportingSettingsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cortanaBriefingAuditRecord":
				from .security_cortana_briefing_audit_record import SecurityCortanaBriefingAuditRecord
				return SecurityCortanaBriefingAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cpsCommonPolicyAuditRecord":
				from .security_cps_common_policy_audit_record import SecurityCpsCommonPolicyAuditRecord
				return SecurityCpsCommonPolicyAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cpsPolicyConfigAuditRecord":
				from .security_cps_policy_config_audit_record import SecurityCpsPolicyConfigAuditRecord
				return SecurityCpsPolicyConfigAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.crmBaseAuditRecord":
				from .security_crm_base_audit_record import SecurityCrmBaseAuditRecord
				return SecurityCrmBaseAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.crmEntityOperationAuditRecord":
				from .security_crm_entity_operation_audit_record import SecurityCrmEntityOperationAuditRecord
				return SecurityCrmEntityOperationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.customerKeyServiceEncryptionAuditRecord":
				from .security_customer_key_service_encryption_audit_record import SecurityCustomerKeyServiceEncryptionAuditRecord
				return SecurityCustomerKeyServiceEncryptionAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dataCenterSecurityBaseAuditRecord":
				from .security_data_center_security_base_audit_record import SecurityDataCenterSecurityBaseAuditRecord
				return SecurityDataCenterSecurityBaseAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dataCenterSecurityCmdletAuditRecord":
				from .security_data_center_security_cmdlet_audit_record import SecurityDataCenterSecurityCmdletAuditRecord
				return SecurityDataCenterSecurityCmdletAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dataGovernanceAuditRecord":
				from .security_data_governance_audit_record import SecurityDataGovernanceAuditRecord
				return SecurityDataGovernanceAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dataInsightsRestApiAuditRecord":
				from .security_data_insights_rest_api_audit_record import SecurityDataInsightsRestApiAuditRecord
				return SecurityDataInsightsRestApiAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dataLakeExportOperationAuditRecord":
				from .security_data_lake_export_operation_audit_record import SecurityDataLakeExportOperationAuditRecord
				return SecurityDataLakeExportOperationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dataShareOperationAuditRecord":
				from .security_data_share_operation_audit_record import SecurityDataShareOperationAuditRecord
				return SecurityDataShareOperationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.defaultAuditData":
				from .security_default_audit_data import SecurityDefaultAuditData
				return SecurityDefaultAuditData.model_validate(data)
			if mapping_key == "#microsoft.graph.security.defenderSecurityAlertBaseRecord":
				from .security_defender_security_alert_base_record import SecurityDefenderSecurityAlertBaseRecord
				return SecurityDefenderSecurityAlertBaseRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.deleteCertificateRecord":
				from .security_delete_certificate_record import SecurityDeleteCertificateRecord
				return SecurityDeleteCertificateRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.disableConsentRecord":
				from .security_disable_consent_record import SecurityDisableConsentRecord
				return SecurityDisableConsentRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.discoveryAuditRecord":
				from .security_discovery_audit_record import SecurityDiscoveryAuditRecord
				return SecurityDiscoveryAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dlpEndpointAuditRecord":
				from .security_dlp_endpoint_audit_record import SecurityDlpEndpointAuditRecord
				return SecurityDlpEndpointAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dlpSensitiveInformationTypeCmdletRecord":
				from .security_dlp_sensitive_information_type_cmdlet_record import SecurityDlpSensitiveInformationTypeCmdletRecord
				return SecurityDlpSensitiveInformationTypeCmdletRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dlpSensitiveInformationTypeRulePackageCmdletRecord":
				from .security_dlp_sensitive_information_type_rule_package_cmdlet_record import SecurityDlpSensitiveInformationTypeRulePackageCmdletRecord
				return SecurityDlpSensitiveInformationTypeRulePackageCmdletRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.downloadCertificateRecord":
				from .security_download_certificate_record import SecurityDownloadCertificateRecord
				return SecurityDownloadCertificateRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dynamics365BusinessCentralAuditRecord":
				from .security_dynamics365_business_central_audit_record import SecurityDynamics365BusinessCentralAuditRecord
				return SecurityDynamics365BusinessCentralAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.enableConsentRecord":
				from .security_enable_consent_record import SecurityEnableConsentRecord
				return SecurityEnableConsentRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.epicSMSLinkRecord":
				from .security_epic_s_m_s_link_record import SecurityEpicSMSLinkRecord
				return SecurityEpicSMSLinkRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.epicSMSSettingsUpdateRecord":
				from .security_epic_s_m_s_settings_update_record import SecurityEpicSMSSettingsUpdateRecord
				return SecurityEpicSMSSettingsUpdateRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.epicSMSUnlinkRecord":
				from .security_epic_s_m_s_unlink_record import SecurityEpicSMSUnlinkRecord
				return SecurityEpicSMSUnlinkRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.exchangeAdminAuditRecord":
				from .security_exchange_admin_audit_record import SecurityExchangeAdminAuditRecord
				return SecurityExchangeAdminAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.exchangeAggregatedMailboxAuditRecord":
				from .security_exchange_aggregated_mailbox_audit_record import SecurityExchangeAggregatedMailboxAuditRecord
				return SecurityExchangeAggregatedMailboxAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.exchangeAggregatedOperationRecord":
				from .security_exchange_aggregated_operation_record import SecurityExchangeAggregatedOperationRecord
				return SecurityExchangeAggregatedOperationRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.exchangeMailboxAuditBaseRecord":
				from .security_exchange_mailbox_audit_base_record import SecurityExchangeMailboxAuditBaseRecord
				return SecurityExchangeMailboxAuditBaseRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.exchangeMailboxAuditGroupRecord":
				from .security_exchange_mailbox_audit_group_record import SecurityExchangeMailboxAuditGroupRecord
				return SecurityExchangeMailboxAuditGroupRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.exchangeMailboxAuditRecord":
				from .security_exchange_mailbox_audit_record import SecurityExchangeMailboxAuditRecord
				return SecurityExchangeMailboxAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.fhirBaseUrlAddRecord":
				from .security_fhir_base_url_add_record import SecurityFhirBaseUrlAddRecord
				return SecurityFhirBaseUrlAddRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.fhirBaseUrlApproveRecord":
				from .security_fhir_base_url_approve_record import SecurityFhirBaseUrlApproveRecord
				return SecurityFhirBaseUrlApproveRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.fhirBaseUrlDeleteRecord":
				from .security_fhir_base_url_delete_record import SecurityFhirBaseUrlDeleteRecord
				return SecurityFhirBaseUrlDeleteRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.fhirBaseUrlUpdateRecord":
				from .security_fhir_base_url_update_record import SecurityFhirBaseUrlUpdateRecord
				return SecurityFhirBaseUrlUpdateRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.healthcareSignalRecord":
				from .security_healthcare_signal_record import SecurityHealthcareSignalRecord
				return SecurityHealthcareSignalRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostedRpaAuditRecord":
				from .security_hosted_rpa_audit_record import SecurityHostedRpaAuditRecord
				return SecurityHostedRpaAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hrSignalAuditRecord":
				from .security_hr_signal_audit_record import SecurityHrSignalAuditRecord
				return SecurityHrSignalAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hygieneEventRecord":
				from .security_hygiene_event_record import SecurityHygieneEventRecord
				return SecurityHygieneEventRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.informationBarrierPolicyApplicationAuditRecord":
				from .security_information_barrier_policy_application_audit_record import SecurityInformationBarrierPolicyApplicationAuditRecord
				return SecurityInformationBarrierPolicyApplicationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.informationWorkerProtectionAuditRecord":
				from .security_information_worker_protection_audit_record import SecurityInformationWorkerProtectionAuditRecord
				return SecurityInformationWorkerProtectionAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.insiderRiskScopedUserInsightsRecord":
				from .security_insider_risk_scoped_user_insights_record import SecurityInsiderRiskScopedUserInsightsRecord
				return SecurityInsiderRiskScopedUserInsightsRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.insiderRiskScopedUsersRecord":
				from .security_insider_risk_scoped_users_record import SecurityInsiderRiskScopedUsersRecord
				return SecurityInsiderRiskScopedUsersRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.irmSecurityAlertRecord":
				from .security_irm_security_alert_record import SecurityIrmSecurityAlertRecord
				return SecurityIrmSecurityAlertRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.irmUserDefinedDetectionRecord":
				from .security_irm_user_defined_detection_record import SecurityIrmUserDefinedDetectionRecord
				return SecurityIrmUserDefinedDetectionRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.kaizalaAuditRecord":
				from .security_kaizala_audit_record import SecurityKaizalaAuditRecord
				return SecurityKaizalaAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.labelAnalyticsAggregateAuditRecord":
				from .security_label_analytics_aggregate_audit_record import SecurityLabelAnalyticsAggregateAuditRecord
				return SecurityLabelAnalyticsAggregateAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.labelContentExplorerAuditRecord":
				from .security_label_content_explorer_audit_record import SecurityLabelContentExplorerAuditRecord
				return SecurityLabelContentExplorerAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.largeContentMetadataAuditRecord":
				from .security_large_content_metadata_audit_record import SecurityLargeContentMetadataAuditRecord
				return SecurityLargeContentMetadataAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.m365ComplianceConnectorAuditRecord":
				from .security_m365_compliance_connector_audit_record import SecurityM365ComplianceConnectorAuditRecord
				return SecurityM365ComplianceConnectorAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.m365DAADAuditRecord":
				from .security_m365_d_a_a_d_audit_record import SecurityM365DAADAuditRecord
				return SecurityM365DAADAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mailSubmissionData":
				from .security_mail_submission_data import SecurityMailSubmissionData
				return SecurityMailSubmissionData.model_validate(data)
			if mapping_key == "#microsoft.graph.security.managedServicesAuditRecord":
				from .security_managed_services_audit_record import SecurityManagedServicesAuditRecord
				return SecurityManagedServicesAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.managedTenantsAuditRecord":
				from .security_managed_tenants_audit_record import SecurityManagedTenantsAuditRecord
				return SecurityManagedTenantsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mapgAlertsAuditRecord":
				from .security_mapg_alerts_audit_record import SecurityMapgAlertsAuditRecord
				return SecurityMapgAlertsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mapgOnboardAuditRecord":
				from .security_mapg_onboard_audit_record import SecurityMapgOnboardAuditRecord
				return SecurityMapgOnboardAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mapgPolicyAuditRecord":
				from .security_mapg_policy_audit_record import SecurityMapgPolicyAuditRecord
				return SecurityMapgPolicyAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mcasAlertsAuditRecord":
				from .security_mcas_alerts_audit_record import SecurityMcasAlertsAuditRecord
				return SecurityMcasAlertsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mdaDataSecuritySignalRecord":
				from .security_mda_data_security_signal_record import SecurityMdaDataSecuritySignalRecord
				return SecurityMdaDataSecuritySignalRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mdatpAuditRecord":
				from .security_mdatp_audit_record import SecurityMdatpAuditRecord
				return SecurityMdatpAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mdcEventsRecord":
				from .security_mdc_events_record import SecurityMdcEventsRecord
				return SecurityMdcEventsRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mdiAuditRecord":
				from .security_mdi_audit_record import SecurityMdiAuditRecord
				return SecurityMdiAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.meshWorldsAuditRecord":
				from .security_mesh_worlds_audit_record import SecurityMeshWorldsAuditRecord
				return SecurityMeshWorldsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoft365BackupBackupItemAuditRecord":
				from .security_microsoft365_backup_backup_item_audit_record import SecurityMicrosoft365BackupBackupItemAuditRecord
				return SecurityMicrosoft365BackupBackupItemAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoft365BackupBackupPolicyAuditRecord":
				from .security_microsoft365_backup_backup_policy_audit_record import SecurityMicrosoft365BackupBackupPolicyAuditRecord
				return SecurityMicrosoft365BackupBackupPolicyAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoft365BackupRestoreItemAuditRecord":
				from .security_microsoft365_backup_restore_item_audit_record import SecurityMicrosoft365BackupRestoreItemAuditRecord
				return SecurityMicrosoft365BackupRestoreItemAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoft365BackupRestoreTaskAuditRecord":
				from .security_microsoft365_backup_restore_task_audit_record import SecurityMicrosoft365BackupRestoreTaskAuditRecord
				return SecurityMicrosoft365BackupRestoreTaskAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftDefenderExpertsBaseAuditRecord":
				from .security_microsoft_defender_experts_base_audit_record import SecurityMicrosoftDefenderExpertsBaseAuditRecord
				return SecurityMicrosoftDefenderExpertsBaseAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftDefenderExpertsXDRAuditRecord":
				from .security_microsoft_defender_experts_x_d_r_audit_record import SecurityMicrosoftDefenderExpertsXDRAuditRecord
				return SecurityMicrosoftDefenderExpertsXDRAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftFlowAuditRecord":
				from .security_microsoft_flow_audit_record import SecurityMicrosoftFlowAuditRecord
				return SecurityMicrosoftFlowAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftFormsAuditRecord":
				from .security_microsoft_forms_audit_record import SecurityMicrosoftFormsAuditRecord
				return SecurityMicrosoftFormsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftGraphDataConnectConsent":
				from .security_microsoft_graph_data_connect_consent import SecurityMicrosoftGraphDataConnectConsent
				return SecurityMicrosoftGraphDataConnectConsent.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftGraphDataConnectOperation":
				from .security_microsoft_graph_data_connect_operation import SecurityMicrosoftGraphDataConnectOperation
				return SecurityMicrosoftGraphDataConnectOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftPurviewDataMapOperationRecord":
				from .security_microsoft_purview_data_map_operation_record import SecurityMicrosoftPurviewDataMapOperationRecord
				return SecurityMicrosoftPurviewDataMapOperationRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftPurviewMetadataPolicyOperationRecord":
				from .security_microsoft_purview_metadata_policy_operation_record import SecurityMicrosoftPurviewMetadataPolicyOperationRecord
				return SecurityMicrosoftPurviewMetadataPolicyOperationRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftPurviewPolicyOperationRecord":
				from .security_microsoft_purview_policy_operation_record import SecurityMicrosoftPurviewPolicyOperationRecord
				return SecurityMicrosoftPurviewPolicyOperationRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftPurviewPrivacyAuditEvent":
				from .security_microsoft_purview_privacy_audit_event import SecurityMicrosoftPurviewPrivacyAuditEvent
				return SecurityMicrosoftPurviewPrivacyAuditEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftStreamAuditRecord":
				from .security_microsoft_stream_audit_record import SecurityMicrosoftStreamAuditRecord
				return SecurityMicrosoftStreamAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftTeamsAdminAuditRecord":
				from .security_microsoft_teams_admin_audit_record import SecurityMicrosoftTeamsAdminAuditRecord
				return SecurityMicrosoftTeamsAdminAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftTeamsAnalyticsAuditRecord":
				from .security_microsoft_teams_analytics_audit_record import SecurityMicrosoftTeamsAnalyticsAuditRecord
				return SecurityMicrosoftTeamsAnalyticsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftTeamsAuditRecord":
				from .security_microsoft_teams_audit_record import SecurityMicrosoftTeamsAuditRecord
				return SecurityMicrosoftTeamsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftTeamsDeviceAuditRecord":
				from .security_microsoft_teams_device_audit_record import SecurityMicrosoftTeamsDeviceAuditRecord
				return SecurityMicrosoftTeamsDeviceAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftTeamsRetentionLabelActionAuditRecord":
				from .security_microsoft_teams_retention_label_action_audit_record import SecurityMicrosoftTeamsRetentionLabelActionAuditRecord
				return SecurityMicrosoftTeamsRetentionLabelActionAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftTeamsSensitivityLabelActionAuditRecord":
				from .security_microsoft_teams_sensitivity_label_action_audit_record import SecurityMicrosoftTeamsSensitivityLabelActionAuditRecord
				return SecurityMicrosoftTeamsSensitivityLabelActionAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.microsoftTeamsShiftsAuditRecord":
				from .security_microsoft_teams_shifts_audit_record import SecurityMicrosoftTeamsShiftsAuditRecord
				return SecurityMicrosoftTeamsShiftsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipAutoLabelExchangeItemAuditRecord":
				from .security_mip_auto_label_exchange_item_audit_record import SecurityMipAutoLabelExchangeItemAuditRecord
				return SecurityMipAutoLabelExchangeItemAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipAutoLabelItemAuditRecord":
				from .security_mip_auto_label_item_audit_record import SecurityMipAutoLabelItemAuditRecord
				return SecurityMipAutoLabelItemAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipAutoLabelPolicyAuditRecord":
				from .security_mip_auto_label_policy_audit_record import SecurityMipAutoLabelPolicyAuditRecord
				return SecurityMipAutoLabelPolicyAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipAutoLabelProgressFeedbackAuditRecord":
				from .security_mip_auto_label_progress_feedback_audit_record import SecurityMipAutoLabelProgressFeedbackAuditRecord
				return SecurityMipAutoLabelProgressFeedbackAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipAutoLabelSharePointItemAuditRecord":
				from .security_mip_auto_label_share_point_item_audit_record import SecurityMipAutoLabelSharePointItemAuditRecord
				return SecurityMipAutoLabelSharePointItemAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipAutoLabelSharePointPolicyLocationAuditRecord":
				from .security_mip_auto_label_share_point_policy_location_audit_record import SecurityMipAutoLabelSharePointPolicyLocationAuditRecord
				return SecurityMipAutoLabelSharePointPolicyLocationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipAutoLabelSimulationSharePointCompletionRecord":
				from .security_mip_auto_label_simulation_share_point_completion_record import SecurityMipAutoLabelSimulationSharePointCompletionRecord
				return SecurityMipAutoLabelSimulationSharePointCompletionRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipAutoLabelSimulationSharePointProgressRecord":
				from .security_mip_auto_label_simulation_share_point_progress_record import SecurityMipAutoLabelSimulationSharePointProgressRecord
				return SecurityMipAutoLabelSimulationSharePointProgressRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipAutoLabelSimulationStatisticsRecord":
				from .security_mip_auto_label_simulation_statistics_record import SecurityMipAutoLabelSimulationStatisticsRecord
				return SecurityMipAutoLabelSimulationStatisticsRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipAutoLabelSimulationStatusRecord":
				from .security_mip_auto_label_simulation_status_record import SecurityMipAutoLabelSimulationStatusRecord
				return SecurityMipAutoLabelSimulationStatusRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipExactDataMatchAuditRecord":
				from .security_mip_exact_data_match_audit_record import SecurityMipExactDataMatchAuditRecord
				return SecurityMipExactDataMatchAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipLabelAnalyticsAuditRecord":
				from .security_mip_label_analytics_audit_record import SecurityMipLabelAnalyticsAuditRecord
				return SecurityMipLabelAnalyticsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mipLabelAuditRecord":
				from .security_mip_label_audit_record import SecurityMipLabelAuditRecord
				return SecurityMipLabelAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mS365DCustomDetectionAuditRecord":
				from .security_m_s365_d_custom_detection_audit_record import SecurityMS365DCustomDetectionAuditRecord
				return SecurityMS365DCustomDetectionAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mS365DIncidentAuditRecord":
				from .security_m_s365_d_incident_audit_record import SecurityMS365DIncidentAuditRecord
				return SecurityMS365DIncidentAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mS365DSuppressionRuleAuditRecord":
				from .security_m_s365_d_suppression_rule_audit_record import SecurityMS365DSuppressionRuleAuditRecord
				return SecurityMS365DSuppressionRuleAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.msdeGeneralSettingsAuditRecord":
				from .security_msde_general_settings_audit_record import SecurityMsdeGeneralSettingsAuditRecord
				return SecurityMsdeGeneralSettingsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.msdeIndicatorsSettingsAuditRecord":
				from .security_msde_indicators_settings_audit_record import SecurityMsdeIndicatorsSettingsAuditRecord
				return SecurityMsdeIndicatorsSettingsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.msdeResponseActionsAuditRecord":
				from .security_msde_response_actions_audit_record import SecurityMsdeResponseActionsAuditRecord
				return SecurityMsdeResponseActionsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.msdeRolesSettingsAuditRecord":
				from .security_msde_roles_settings_audit_record import SecurityMsdeRolesSettingsAuditRecord
				return SecurityMsdeRolesSettingsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.msticNationStateNotificationRecord":
				from .security_mstic_nation_state_notification_record import SecurityMsticNationStateNotificationRecord
				return SecurityMsticNationStateNotificationRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.multiStageDispositionAuditRecord":
				from .security_multi_stage_disposition_audit_record import SecurityMultiStageDispositionAuditRecord
				return SecurityMultiStageDispositionAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.myAnalyticsSettingsAuditRecord":
				from .security_my_analytics_settings_audit_record import SecurityMyAnalyticsSettingsAuditRecord
				return SecurityMyAnalyticsSettingsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.officeNativeAuditRecord":
				from .security_office_native_audit_record import SecurityOfficeNativeAuditRecord
				return SecurityOfficeNativeAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.omePortalAuditRecord":
				from .security_ome_portal_audit_record import SecurityOmePortalAuditRecord
				return SecurityOmePortalAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.oneDriveAuditRecord":
				from .security_one_drive_audit_record import SecurityOneDriveAuditRecord
				return SecurityOneDriveAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.onPremisesFileShareScannerDlpAuditRecord":
				from .security_on_premises_file_share_scanner_dlp_audit_record import SecurityOnPremisesFileShareScannerDlpAuditRecord
				return SecurityOnPremisesFileShareScannerDlpAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.onPremisesScannerDlpAuditRecord":
				from .security_on_premises_scanner_dlp_audit_record import SecurityOnPremisesScannerDlpAuditRecord
				return SecurityOnPremisesScannerDlpAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.onPremisesSharePointScannerDlpAuditRecord":
				from .security_on_premises_share_point_scanner_dlp_audit_record import SecurityOnPremisesSharePointScannerDlpAuditRecord
				return SecurityOnPremisesSharePointScannerDlpAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.owaGetAccessTokenForResourceAuditRecord":
				from .security_owa_get_access_token_for_resource_audit_record import SecurityOwaGetAccessTokenForResourceAuditRecord
				return SecurityOwaGetAccessTokenForResourceAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.peopleAdminSettingsAuditRecord":
				from .security_people_admin_settings_audit_record import SecurityPeopleAdminSettingsAuditRecord
				return SecurityPeopleAdminSettingsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.physicalBadgingSignalAuditRecord":
				from .security_physical_badging_signal_audit_record import SecurityPhysicalBadgingSignalAuditRecord
				return SecurityPhysicalBadgingSignalAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.plannerCopyPlanAuditRecord":
				from .security_planner_copy_plan_audit_record import SecurityPlannerCopyPlanAuditRecord
				return SecurityPlannerCopyPlanAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.plannerPlanAuditRecord":
				from .security_planner_plan_audit_record import SecurityPlannerPlanAuditRecord
				return SecurityPlannerPlanAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.plannerPlanListAuditRecord":
				from .security_planner_plan_list_audit_record import SecurityPlannerPlanListAuditRecord
				return SecurityPlannerPlanListAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.plannerRosterAuditRecord":
				from .security_planner_roster_audit_record import SecurityPlannerRosterAuditRecord
				return SecurityPlannerRosterAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.plannerRosterSensitivityLabelAuditRecord":
				from .security_planner_roster_sensitivity_label_audit_record import SecurityPlannerRosterSensitivityLabelAuditRecord
				return SecurityPlannerRosterSensitivityLabelAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.plannerTaskAuditRecord":
				from .security_planner_task_audit_record import SecurityPlannerTaskAuditRecord
				return SecurityPlannerTaskAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.plannerTaskListAuditRecord":
				from .security_planner_task_list_audit_record import SecurityPlannerTaskListAuditRecord
				return SecurityPlannerTaskListAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.plannerTenantSettingsAuditRecord":
				from .security_planner_tenant_settings_audit_record import SecurityPlannerTenantSettingsAuditRecord
				return SecurityPlannerTenantSettingsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.powerAppsAuditAppRecord":
				from .security_power_apps_audit_app_record import SecurityPowerAppsAuditAppRecord
				return SecurityPowerAppsAuditAppRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.powerAppsAuditPlanRecord":
				from .security_power_apps_audit_plan_record import SecurityPowerAppsAuditPlanRecord
				return SecurityPowerAppsAuditPlanRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.powerAppsAuditResourceRecord":
				from .security_power_apps_audit_resource_record import SecurityPowerAppsAuditResourceRecord
				return SecurityPowerAppsAuditResourceRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.powerBiAuditRecord":
				from .security_power_bi_audit_record import SecurityPowerBiAuditRecord
				return SecurityPowerBiAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.powerBiDlpAuditRecord":
				from .security_power_bi_dlp_audit_record import SecurityPowerBiDlpAuditRecord
				return SecurityPowerBiDlpAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.powerPagesSiteAuditRecord":
				from .security_power_pages_site_audit_record import SecurityPowerPagesSiteAuditRecord
				return SecurityPowerPagesSiteAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.powerPlatformAdminDlpAuditRecord":
				from .security_power_platform_admin_dlp_audit_record import SecurityPowerPlatformAdminDlpAuditRecord
				return SecurityPowerPlatformAdminDlpAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.powerPlatformAdminEnvironmentAuditRecord":
				from .security_power_platform_admin_environment_audit_record import SecurityPowerPlatformAdminEnvironmentAuditRecord
				return SecurityPowerPlatformAdminEnvironmentAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.powerPlatformAdministratorActivityRecord":
				from .security_power_platform_administrator_activity_record import SecurityPowerPlatformAdministratorActivityRecord
				return SecurityPowerPlatformAdministratorActivityRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.powerPlatformLockboxResourceAccessRequestAuditRecord":
				from .security_power_platform_lockbox_resource_access_request_audit_record import SecurityPowerPlatformLockboxResourceAccessRequestAuditRecord
				return SecurityPowerPlatformLockboxResourceAccessRequestAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.powerPlatformLockboxResourceCommandAuditRecord":
				from .security_power_platform_lockbox_resource_command_audit_record import SecurityPowerPlatformLockboxResourceCommandAuditRecord
				return SecurityPowerPlatformLockboxResourceCommandAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.powerPlatformServiceActivityAuditRecord":
				from .security_power_platform_service_activity_audit_record import SecurityPowerPlatformServiceActivityAuditRecord
				return SecurityPowerPlatformServiceActivityAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.privacyDataMatchAuditRecord":
				from .security_privacy_data_match_audit_record import SecurityPrivacyDataMatchAuditRecord
				return SecurityPrivacyDataMatchAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.privacyDataMinimizationRecord":
				from .security_privacy_data_minimization_record import SecurityPrivacyDataMinimizationRecord
				return SecurityPrivacyDataMinimizationRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.privacyDigestEmailRecord":
				from .security_privacy_digest_email_record import SecurityPrivacyDigestEmailRecord
				return SecurityPrivacyDigestEmailRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.privacyOpenAccessAuditRecord":
				from .security_privacy_open_access_audit_record import SecurityPrivacyOpenAccessAuditRecord
				return SecurityPrivacyOpenAccessAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.privacyPortalAuditRecord":
				from .security_privacy_portal_audit_record import SecurityPrivacyPortalAuditRecord
				return SecurityPrivacyPortalAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.privacyRemediationActionRecord":
				from .security_privacy_remediation_action_record import SecurityPrivacyRemediationActionRecord
				return SecurityPrivacyRemediationActionRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.privacyRemediationRecord":
				from .security_privacy_remediation_record import SecurityPrivacyRemediationRecord
				return SecurityPrivacyRemediationRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.privacyTenantAuditHistoryRecord":
				from .security_privacy_tenant_audit_history_record import SecurityPrivacyTenantAuditHistoryRecord
				return SecurityPrivacyTenantAuditHistoryRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.projectAuditRecord":
				from .security_project_audit_record import SecurityProjectAuditRecord
				return SecurityProjectAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.projectForTheWebAssignedToMeSettingsAuditRecord":
				from .security_project_for_the_web_assigned_to_me_settings_audit_record import SecurityProjectForTheWebAssignedToMeSettingsAuditRecord
				return SecurityProjectForTheWebAssignedToMeSettingsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.projectForTheWebProjectAuditRecord":
				from .security_project_for_the_web_project_audit_record import SecurityProjectForTheWebProjectAuditRecord
				return SecurityProjectForTheWebProjectAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.projectForTheWebProjectSettingsAuditRecord":
				from .security_project_for_the_web_project_settings_audit_record import SecurityProjectForTheWebProjectSettingsAuditRecord
				return SecurityProjectForTheWebProjectSettingsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.projectForTheWebRoadmapAuditRecord":
				from .security_project_for_the_web_roadmap_audit_record import SecurityProjectForTheWebRoadmapAuditRecord
				return SecurityProjectForTheWebRoadmapAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.projectForTheWebRoadmapItemAuditRecord":
				from .security_project_for_the_web_roadmap_item_audit_record import SecurityProjectForTheWebRoadmapItemAuditRecord
				return SecurityProjectForTheWebRoadmapItemAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.projectForTheWebRoadmapSettingsAuditRecord":
				from .security_project_for_the_web_roadmap_settings_audit_record import SecurityProjectForTheWebRoadmapSettingsAuditRecord
				return SecurityProjectForTheWebRoadmapSettingsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.projectForTheWebTaskAuditRecord":
				from .security_project_for_the_web_task_audit_record import SecurityProjectForTheWebTaskAuditRecord
				return SecurityProjectForTheWebTaskAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.publicFolderAuditRecord":
				from .security_public_folder_audit_record import SecurityPublicFolderAuditRecord
				return SecurityPublicFolderAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.purviewInsiderRiskAlertsRecord":
				from .security_purview_insider_risk_alerts_record import SecurityPurviewInsiderRiskAlertsRecord
				return SecurityPurviewInsiderRiskAlertsRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.purviewInsiderRiskCasesRecord":
				from .security_purview_insider_risk_cases_record import SecurityPurviewInsiderRiskCasesRecord
				return SecurityPurviewInsiderRiskCasesRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.quarantineAuditRecord":
				from .security_quarantine_audit_record import SecurityQuarantineAuditRecord
				return SecurityQuarantineAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.recordsManagementAuditRecord":
				from .security_records_management_audit_record import SecurityRecordsManagementAuditRecord
				return SecurityRecordsManagementAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.retentionPolicyAuditRecord":
				from .security_retention_policy_audit_record import SecurityRetentionPolicyAuditRecord
				return SecurityRetentionPolicyAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.scoreEvidence":
				from .security_score_evidence import SecurityScoreEvidence
				return SecurityScoreEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.scorePlatformGenericAuditRecord":
				from .security_score_platform_generic_audit_record import SecurityScorePlatformGenericAuditRecord
				return SecurityScorePlatformGenericAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.scriptRunAuditRecord":
				from .security_script_run_audit_record import SecurityScriptRunAuditRecord
				return SecurityScriptRunAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.searchAuditRecord":
				from .security_search_audit_record import SecuritySearchAuditRecord
				return SecuritySearchAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.securityComplianceAlertRecord":
				from .security_security_compliance_alert_record import SecuritySecurityComplianceAlertRecord
				return SecuritySecurityComplianceAlertRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.securityComplianceCenterEOPCmdletAuditRecord":
				from .security_security_compliance_center_e_o_p_cmdlet_audit_record import SecuritySecurityComplianceCenterEOPCmdletAuditRecord
				return SecuritySecurityComplianceCenterEOPCmdletAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.securityComplianceInsightsAuditRecord":
				from .security_security_compliance_insights_audit_record import SecuritySecurityComplianceInsightsAuditRecord
				return SecuritySecurityComplianceInsightsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.securityComplianceRBACAuditRecord":
				from .security_security_compliance_r_b_a_c_audit_record import SecuritySecurityComplianceRBACAuditRecord
				return SecuritySecurityComplianceRBACAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.securityComplianceUserChangeAuditRecord":
				from .security_security_compliance_user_change_audit_record import SecuritySecurityComplianceUserChangeAuditRecord
				return SecuritySecurityComplianceUserChangeAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sharePointAppPermissionOperationAuditRecord":
				from .security_share_point_app_permission_operation_audit_record import SecuritySharePointAppPermissionOperationAuditRecord
				return SecuritySharePointAppPermissionOperationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sharePointAuditRecord":
				from .security_share_point_audit_record import SecuritySharePointAuditRecord
				return SecuritySharePointAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sharePointCommentOperationAuditRecord":
				from .security_share_point_comment_operation_audit_record import SecuritySharePointCommentOperationAuditRecord
				return SecuritySharePointCommentOperationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sharePointContentTypeOperationAuditRecord":
				from .security_share_point_content_type_operation_audit_record import SecuritySharePointContentTypeOperationAuditRecord
				return SecuritySharePointContentTypeOperationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sharePointESignatureAuditRecord":
				from .security_share_point_e_signature_audit_record import SecuritySharePointESignatureAuditRecord
				return SecuritySharePointESignatureAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sharePointFieldOperationAuditRecord":
				from .security_share_point_field_operation_audit_record import SecuritySharePointFieldOperationAuditRecord
				return SecuritySharePointFieldOperationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sharePointFileOperationAuditRecord":
				from .security_share_point_file_operation_audit_record import SecuritySharePointFileOperationAuditRecord
				return SecuritySharePointFileOperationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sharePointListOperationAuditRecord":
				from .security_share_point_list_operation_audit_record import SecuritySharePointListOperationAuditRecord
				return SecuritySharePointListOperationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sharePointSharingOperationAuditRecord":
				from .security_share_point_sharing_operation_audit_record import SecuritySharePointSharingOperationAuditRecord
				return SecuritySharePointSharingOperationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.skypeForBusinessBaseAuditRecord":
				from .security_skype_for_business_base_audit_record import SecuritySkypeForBusinessBaseAuditRecord
				return SecuritySkypeForBusinessBaseAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.skypeForBusinessCmdletsAuditRecord":
				from .security_skype_for_business_cmdlets_audit_record import SecuritySkypeForBusinessCmdletsAuditRecord
				return SecuritySkypeForBusinessCmdletsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.skypeForBusinessPSTNUsageAuditRecord":
				from .security_skype_for_business_p_s_t_n_usage_audit_record import SecuritySkypeForBusinessPSTNUsageAuditRecord
				return SecuritySkypeForBusinessPSTNUsageAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.skypeForBusinessUsersBlockedAuditRecord":
				from .security_skype_for_business_users_blocked_audit_record import SecuritySkypeForBusinessUsersBlockedAuditRecord
				return SecuritySkypeForBusinessUsersBlockedAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.smsCreatePhoneNumberRecord":
				from .security_sms_create_phone_number_record import SecuritySmsCreatePhoneNumberRecord
				return SecuritySmsCreatePhoneNumberRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.smsDeletePhoneNumberRecord":
				from .security_sms_delete_phone_number_record import SecuritySmsDeletePhoneNumberRecord
				return SecuritySmsDeletePhoneNumberRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.supervisoryReviewDayXInsightsAuditRecord":
				from .security_supervisory_review_day_x_insights_audit_record import SecuritySupervisoryReviewDayXInsightsAuditRecord
				return SecuritySupervisoryReviewDayXInsightsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.syntheticProbeAuditRecord":
				from .security_synthetic_probe_audit_record import SecuritySyntheticProbeAuditRecord
				return SecuritySyntheticProbeAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.teamsEasyApprovalsAuditRecord":
				from .security_teams_easy_approvals_audit_record import SecurityTeamsEasyApprovalsAuditRecord
				return SecurityTeamsEasyApprovalsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.teamsHealthcareAuditRecord":
				from .security_teams_healthcare_audit_record import SecurityTeamsHealthcareAuditRecord
				return SecurityTeamsHealthcareAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.teamsUpdatesAuditRecord":
				from .security_teams_updates_audit_record import SecurityTeamsUpdatesAuditRecord
				return SecurityTeamsUpdatesAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.tenantAllowBlockListAuditRecord":
				from .security_tenant_allow_block_list_audit_record import SecurityTenantAllowBlockListAuditRecord
				return SecurityTenantAllowBlockListAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.threatFinderAuditRecord":
				from .security_threat_finder_audit_record import SecurityThreatFinderAuditRecord
				return SecurityThreatFinderAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.threatIntelligenceAtpContentData":
				from .security_threat_intelligence_atp_content_data import SecurityThreatIntelligenceAtpContentData
				return SecurityThreatIntelligenceAtpContentData.model_validate(data)
			if mapping_key == "#microsoft.graph.security.threatIntelligenceMailData":
				from .security_threat_intelligence_mail_data import SecurityThreatIntelligenceMailData
				return SecurityThreatIntelligenceMailData.model_validate(data)
			if mapping_key == "#microsoft.graph.security.threatIntelligenceUrlClickData":
				from .security_threat_intelligence_url_click_data import SecurityThreatIntelligenceUrlClickData
				return SecurityThreatIntelligenceUrlClickData.model_validate(data)
			if mapping_key == "#microsoft.graph.security.todoAuditRecord":
				from .security_todo_audit_record import SecurityTodoAuditRecord
				return SecurityTodoAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.uamOperationAuditRecord":
				from .security_uam_operation_audit_record import SecurityUamOperationAuditRecord
				return SecurityUamOperationAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.unifiedGroupAuditRecord":
				from .security_unified_group_audit_record import SecurityUnifiedGroupAuditRecord
				return SecurityUnifiedGroupAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.unifiedSimulationMatchedItemAuditRecord":
				from .security_unified_simulation_matched_item_audit_record import SecurityUnifiedSimulationMatchedItemAuditRecord
				return SecurityUnifiedSimulationMatchedItemAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.unifiedSimulationSummaryAuditRecord":
				from .security_unified_simulation_summary_audit_record import SecurityUnifiedSimulationSummaryAuditRecord
				return SecurityUnifiedSimulationSummaryAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.uploadCertificateRecord":
				from .security_upload_certificate_record import SecurityUploadCertificateRecord
				return SecurityUploadCertificateRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.urbacAssignmentAuditRecord":
				from .security_urbac_assignment_audit_record import SecurityUrbacAssignmentAuditRecord
				return SecurityUrbacAssignmentAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.urbacEnableStateAuditRecord":
				from .security_urbac_enable_state_audit_record import SecurityUrbacEnableStateAuditRecord
				return SecurityUrbacEnableStateAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.urbacRoleAuditRecord":
				from .security_urbac_role_audit_record import SecurityUrbacRoleAuditRecord
				return SecurityUrbacRoleAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.userTrainingAuditRecord":
				from .security_user_training_audit_record import SecurityUserTrainingAuditRecord
				return SecurityUserTrainingAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vfamBasePolicyAuditRecord":
				from .security_vfam_base_policy_audit_record import SecurityVfamBasePolicyAuditRecord
				return SecurityVfamBasePolicyAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vfamCreatePolicyAuditRecord":
				from .security_vfam_create_policy_audit_record import SecurityVfamCreatePolicyAuditRecord
				return SecurityVfamCreatePolicyAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vfamDeletePolicyAuditRecord":
				from .security_vfam_delete_policy_audit_record import SecurityVfamDeletePolicyAuditRecord
				return SecurityVfamDeletePolicyAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vfamUpdatePolicyAuditRecord":
				from .security_vfam_update_policy_audit_record import SecurityVfamUpdatePolicyAuditRecord
				return SecurityVfamUpdatePolicyAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vivaGoalsAuditRecord":
				from .security_viva_goals_audit_record import SecurityVivaGoalsAuditRecord
				return SecurityVivaGoalsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vivaLearningAdminAuditRecord":
				from .security_viva_learning_admin_audit_record import SecurityVivaLearningAdminAuditRecord
				return SecurityVivaLearningAdminAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vivaLearningAuditRecord":
				from .security_viva_learning_audit_record import SecurityVivaLearningAuditRecord
				return SecurityVivaLearningAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vivaPulseAdminAuditRecord":
				from .security_viva_pulse_admin_audit_record import SecurityVivaPulseAdminAuditRecord
				return SecurityVivaPulseAdminAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vivaPulseOrganizerAuditRecord":
				from .security_viva_pulse_organizer_audit_record import SecurityVivaPulseOrganizerAuditRecord
				return SecurityVivaPulseOrganizerAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vivaPulseReportAuditRecord":
				from .security_viva_pulse_report_audit_record import SecurityVivaPulseReportAuditRecord
				return SecurityVivaPulseReportAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vivaPulseResponseAuditRecord":
				from .security_viva_pulse_response_audit_record import SecurityVivaPulseResponseAuditRecord
				return SecurityVivaPulseResponseAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.wdatpAlertsAuditRecord":
				from .security_wdatp_alerts_audit_record import SecurityWdatpAlertsAuditRecord
				return SecurityWdatpAlertsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.windows365CustomerLockboxAuditRecord":
				from .security_windows365_customer_lockbox_audit_record import SecurityWindows365CustomerLockboxAuditRecord
				return SecurityWindows365CustomerLockboxAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.workplaceAnalyticsAuditRecord":
				from .security_workplace_analytics_audit_record import SecurityWorkplaceAnalyticsAuditRecord
				return SecurityWorkplaceAnalyticsAuditRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.yammerAuditRecord":
				from .security_yammer_audit_record import SecurityYammerAuditRecord
				return SecurityYammerAuditRecord.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

