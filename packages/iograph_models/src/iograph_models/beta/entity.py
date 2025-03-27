from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class Entity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
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
			if mapping_key == "#microsoft.graph.accessPackage":
				from .access_package import AccessPackage
				return AccessPackage.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageAssignment":
				from .access_package_assignment import AccessPackageAssignment
				return AccessPackageAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageAssignmentPolicy":
				from .access_package_assignment_policy import AccessPackageAssignmentPolicy
				return AccessPackageAssignmentPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageAssignmentRequest":
				from .access_package_assignment_request import AccessPackageAssignmentRequest
				return AccessPackageAssignmentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageAssignmentResourceRole":
				from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
				return AccessPackageAssignmentResourceRole.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageCatalog":
				from .access_package_catalog import AccessPackageCatalog
				return AccessPackageCatalog.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageResource":
				from .access_package_resource import AccessPackageResource
				return AccessPackageResource.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageResourceEnvironment":
				from .access_package_resource_environment import AccessPackageResourceEnvironment
				return AccessPackageResourceEnvironment.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageResourceRequest":
				from .access_package_resource_request import AccessPackageResourceRequest
				return AccessPackageResourceRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageResourceRole":
				from .access_package_resource_role import AccessPackageResourceRole
				return AccessPackageResourceRole.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageResourceRoleScope":
				from .access_package_resource_role_scope import AccessPackageResourceRoleScope
				return AccessPackageResourceRoleScope.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageResourceScope":
				from .access_package_resource_scope import AccessPackageResourceScope
				return AccessPackageResourceScope.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageSubject":
				from .access_package_subject import AccessPackageSubject
				return AccessPackageSubject.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReview":
				from .access_review import AccessReview
				return AccessReview.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReviewDecision":
				from .access_review_decision import AccessReviewDecision
				return AccessReviewDecision.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReviewHistoryDefinition":
				from .access_review_history_definition import AccessReviewHistoryDefinition
				return AccessReviewHistoryDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReviewHistoryInstance":
				from .access_review_history_instance import AccessReviewHistoryInstance
				return AccessReviewHistoryInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReviewInstance":
				from .access_review_instance import AccessReviewInstance
				return AccessReviewInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReviewInstanceDecisionItem":
				from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
				return AccessReviewInstanceDecisionItem.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReviewPolicy":
				from .access_review_policy import AccessReviewPolicy
				return AccessReviewPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReviewReviewer":
				from .access_review_reviewer import AccessReviewReviewer
				return AccessReviewReviewer.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReviewScheduleDefinition":
				from .access_review_schedule_definition import AccessReviewScheduleDefinition
				return AccessReviewScheduleDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReviewSet":
				from .access_review_set import AccessReviewSet
				return AccessReviewSet.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReviewStage":
				from .access_review_stage import AccessReviewStage
				return AccessReviewStage.model_validate(data)
			if mapping_key == "#microsoft.graph.activeUsersMetric":
				from .active_users_metric import ActiveUsersMetric
				return ActiveUsersMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.activityHistoryItem":
				from .activity_history_item import ActivityHistoryItem
				return ActivityHistoryItem.model_validate(data)
			if mapping_key == "#microsoft.graph.activityStatistics":
				from .activity_statistics import ActivityStatistics
				return ActivityStatistics.model_validate(data)
			if mapping_key == "#microsoft.graph.callActivityStatistics":
				from .call_activity_statistics import CallActivityStatistics
				return CallActivityStatistics.model_validate(data)
			if mapping_key == "#microsoft.graph.chatActivityStatistics":
				from .chat_activity_statistics import ChatActivityStatistics
				return ChatActivityStatistics.model_validate(data)
			if mapping_key == "#microsoft.graph.emailActivityStatistics":
				from .email_activity_statistics import EmailActivityStatistics
				return EmailActivityStatistics.model_validate(data)
			if mapping_key == "#microsoft.graph.focusActivityStatistics":
				from .focus_activity_statistics import FocusActivityStatistics
				return FocusActivityStatistics.model_validate(data)
			if mapping_key == "#microsoft.graph.meetingActivityStatistics":
				from .meeting_activity_statistics import MeetingActivityStatistics
				return MeetingActivityStatistics.model_validate(data)
			if mapping_key == "#microsoft.graph.adminAppsAndServices":
				from .admin_apps_and_services import AdminAppsAndServices
				return AdminAppsAndServices.model_validate(data)
			if mapping_key == "#microsoft.graph.adminConsentRequestPolicy":
				from .admin_consent_request_policy import AdminConsentRequestPolicy
				return AdminConsentRequestPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.adminDynamics":
				from .admin_dynamics import AdminDynamics
				return AdminDynamics.model_validate(data)
			if mapping_key == "#microsoft.graph.adminForms":
				from .admin_forms import AdminForms
				return AdminForms.model_validate(data)
			if mapping_key == "#microsoft.graph.adminMicrosoft365Apps":
				from .admin_microsoft365_apps import AdminMicrosoft365Apps
				return AdminMicrosoft365Apps.model_validate(data)
			if mapping_key == "#microsoft.graph.adminReportSettings":
				from .admin_report_settings import AdminReportSettings
				return AdminReportSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.adminTodo":
				from .admin_todo import AdminTodo
				return AdminTodo.model_validate(data)
			if mapping_key == "#microsoft.graph.adminWindows":
				from .admin_windows import AdminWindows
				return AdminWindows.model_validate(data)
			if mapping_key == "#microsoft.graph.adminWindowsUpdates":
				from .admin_windows_updates import AdminWindowsUpdates
				return AdminWindowsUpdates.model_validate(data)
			if mapping_key == "#microsoft.graph.advancedThreatProtectionOnboardingDeviceSettingState":
				from .advanced_threat_protection_onboarding_device_setting_state import AdvancedThreatProtectionOnboardingDeviceSettingState
				return AdvancedThreatProtectionOnboardingDeviceSettingState.model_validate(data)
			if mapping_key == "#microsoft.graph.advancedThreatProtectionOnboardingStateSummary":
				from .advanced_threat_protection_onboarding_state_summary import AdvancedThreatProtectionOnboardingStateSummary
				return AdvancedThreatProtectionOnboardingStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.agreement":
				from .agreement import Agreement
				return Agreement.model_validate(data)
			if mapping_key == "#microsoft.graph.agreementAcceptance":
				from .agreement_acceptance import AgreementAcceptance
				return AgreementAcceptance.model_validate(data)
			if mapping_key == "#microsoft.graph.agreementFileProperties":
				from .agreement_file_properties import AgreementFileProperties
				return AgreementFileProperties.model_validate(data)
			if mapping_key == "#microsoft.graph.agreementFile":
				from .agreement_file import AgreementFile
				return AgreementFile.model_validate(data)
			if mapping_key == "#microsoft.graph.agreementFileLocalization":
				from .agreement_file_localization import AgreementFileLocalization
				return AgreementFileLocalization.model_validate(data)
			if mapping_key == "#microsoft.graph.agreementFileVersion":
				from .agreement_file_version import AgreementFileVersion
				return AgreementFileVersion.model_validate(data)
			if mapping_key == "#microsoft.graph.aiInteraction":
				from .ai_interaction import AiInteraction
				return AiInteraction.model_validate(data)
			if mapping_key == "#microsoft.graph.aiInteractionHistory":
				from .ai_interaction_history import AiInteractionHistory
				return AiInteractionHistory.model_validate(data)
			if mapping_key == "#microsoft.graph.aiUser":
				from .ai_user import AiUser
				return AiUser.model_validate(data)
			if mapping_key == "#microsoft.graph.alert":
				from .alert import Alert
				return Alert.model_validate(data)
			if mapping_key == "#microsoft.graph.allowedDataLocation":
				from .allowed_data_location import AllowedDataLocation
				return AllowedDataLocation.model_validate(data)
			if mapping_key == "#microsoft.graph.allowedValue":
				from .allowed_value import AllowedValue
				return AllowedValue.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceComplianceLocalActionBase":
				from .android_device_compliance_local_action_base import AndroidDeviceComplianceLocalActionBase
				return AndroidDeviceComplianceLocalActionBase.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceComplianceLocalActionLockDevice":
				from .android_device_compliance_local_action_lock_device import AndroidDeviceComplianceLocalActionLockDevice
				return AndroidDeviceComplianceLocalActionLockDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceComplianceLocalActionLockDeviceWithPasscode":
				from .android_device_compliance_local_action_lock_device_with_passcode import AndroidDeviceComplianceLocalActionLockDeviceWithPasscode
				return AndroidDeviceComplianceLocalActionLockDeviceWithPasscode.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerEnrollmentProfile":
				from .android_device_owner_enrollment_profile import AndroidDeviceOwnerEnrollmentProfile
				return AndroidDeviceOwnerEnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkAppConfigurationSchema":
				from .android_for_work_app_configuration_schema import AndroidForWorkAppConfigurationSchema
				return AndroidForWorkAppConfigurationSchema.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkEnrollmentProfile":
				from .android_for_work_enrollment_profile import AndroidForWorkEnrollmentProfile
				return AndroidForWorkEnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkSettings":
				from .android_for_work_settings import AndroidForWorkSettings
				return AndroidForWorkSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.androidManagedStoreAccountEnterpriseSettings":
				from .android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings
				return AndroidManagedStoreAccountEnterpriseSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.androidManagedStoreAppConfigurationSchema":
				from .android_managed_store_app_configuration_schema import AndroidManagedStoreAppConfigurationSchema
				return AndroidManagedStoreAppConfigurationSchema.model_validate(data)
			if mapping_key == "#microsoft.graph.appConsentApprovalRoute":
				from .app_consent_approval_route import AppConsentApprovalRoute
				return AppConsentApprovalRoute.model_validate(data)
			if mapping_key == "#microsoft.graph.appConsentRequest":
				from .app_consent_request import AppConsentRequest
				return AppConsentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.appCredentialSignInActivity":
				from .app_credential_sign_in_activity import AppCredentialSignInActivity
				return AppCredentialSignInActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.appleEnrollmentProfileAssignment":
				from .apple_enrollment_profile_assignment import AppleEnrollmentProfileAssignment
				return AppleEnrollmentProfileAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.applePushNotificationCertificate":
				from .apple_push_notification_certificate import ApplePushNotificationCertificate
				return ApplePushNotificationCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.appleUserInitiatedEnrollmentProfile":
				from .apple_user_initiated_enrollment_profile import AppleUserInitiatedEnrollmentProfile
				return AppleUserInitiatedEnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.applicationSegment":
				from .application_segment import ApplicationSegment
				return ApplicationSegment.model_validate(data)
			if mapping_key == "#microsoft.graph.ipApplicationSegment":
				from .ip_application_segment import IpApplicationSegment
				return IpApplicationSegment.model_validate(data)
			if mapping_key == "#microsoft.graph.webApplicationSegment":
				from .web_application_segment import WebApplicationSegment
				return WebApplicationSegment.model_validate(data)
			if mapping_key == "#microsoft.graph.applicationSignInDetailedSummary":
				from .application_sign_in_detailed_summary import ApplicationSignInDetailedSummary
				return ApplicationSignInDetailedSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.applicationSignInSummary":
				from .application_sign_in_summary import ApplicationSignInSummary
				return ApplicationSignInSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.applicationTemplate":
				from .application_template import ApplicationTemplate
				return ApplicationTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.appLogCollectionRequest":
				from .app_log_collection_request import AppLogCollectionRequest
				return AppLogCollectionRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.approval":
				from .approval import Approval
				return Approval.model_validate(data)
			if mapping_key == "#microsoft.graph.approvalItem":
				from .approval_item import ApprovalItem
				return ApprovalItem.model_validate(data)
			if mapping_key == "#microsoft.graph.approvalItemRequest":
				from .approval_item_request import ApprovalItemRequest
				return ApprovalItemRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.approvalItemResponse":
				from .approval_item_response import ApprovalItemResponse
				return ApprovalItemResponse.model_validate(data)
			if mapping_key == "#microsoft.graph.approvalOperation":
				from .approval_operation import ApprovalOperation
				return ApprovalOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.approvalSolution":
				from .approval_solution import ApprovalSolution
				return ApprovalSolution.model_validate(data)
			if mapping_key == "#microsoft.graph.approvalStep":
				from .approval_step import ApprovalStep
				return ApprovalStep.model_validate(data)
			if mapping_key == "#microsoft.graph.approvalWorkflowProvider":
				from .approval_workflow_provider import ApprovalWorkflowProvider
				return ApprovalWorkflowProvider.model_validate(data)
			if mapping_key == "#microsoft.graph.appScope":
				from .app_scope import AppScope
				return AppScope.model_validate(data)
			if mapping_key == "#microsoft.graph.customAppScope":
				from .custom_app_scope import CustomAppScope
				return CustomAppScope.model_validate(data)
			if mapping_key == "#microsoft.graph.appVulnerabilityManagedDevice":
				from .app_vulnerability_managed_device import AppVulnerabilityManagedDevice
				return AppVulnerabilityManagedDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.appVulnerabilityMobileApp":
				from .app_vulnerability_mobile_app import AppVulnerabilityMobileApp
				return AppVulnerabilityMobileApp.model_validate(data)
			if mapping_key == "#microsoft.graph.assignedComputeInstanceDetails":
				from .assigned_compute_instance_details import AssignedComputeInstanceDetails
				return AssignedComputeInstanceDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.assignmentFilterEvaluationStatusDetails":
				from .assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetails
				return AssignmentFilterEvaluationStatusDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.attachment":
				from .attachment import Attachment
				return Attachment.model_validate(data)
			if mapping_key == "#microsoft.graph.fileAttachment":
				from .file_attachment import FileAttachment
				return FileAttachment.model_validate(data)
			if mapping_key == "#microsoft.graph.itemAttachment":
				from .item_attachment import ItemAttachment
				return ItemAttachment.model_validate(data)
			if mapping_key == "#microsoft.graph.referenceAttachment":
				from .reference_attachment import ReferenceAttachment
				return ReferenceAttachment.model_validate(data)
			if mapping_key == "#microsoft.graph.attachmentBase":
				from .attachment_base import AttachmentBase
				return AttachmentBase.model_validate(data)
			if mapping_key == "#microsoft.graph.taskFileAttachment":
				from .task_file_attachment import TaskFileAttachment
				return TaskFileAttachment.model_validate(data)
			if mapping_key == "#microsoft.graph.attachmentSession":
				from .attachment_session import AttachmentSession
				return AttachmentSession.model_validate(data)
			if mapping_key == "#microsoft.graph.attackSimulationRoot":
				from .attack_simulation_root import AttackSimulationRoot
				return AttackSimulationRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.attendanceRecord":
				from .attendance_record import AttendanceRecord
				return AttendanceRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.attributeMappingFunctionSchema":
				from .attribute_mapping_function_schema import AttributeMappingFunctionSchema
				return AttributeMappingFunctionSchema.model_validate(data)
			if mapping_key == "#microsoft.graph.attributeSet":
				from .attribute_set import AttributeSet
				return AttributeSet.model_validate(data)
			if mapping_key == "#microsoft.graph.audioRoutingGroup":
				from .audio_routing_group import AudioRoutingGroup
				return AudioRoutingGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.auditEvent":
				from .audit_event import AuditEvent
				return AuditEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.authentication":
				from .authentication import Authentication
				return Authentication.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationCombinationConfiguration":
				from .authentication_combination_configuration import AuthenticationCombinationConfiguration
				return AuthenticationCombinationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.fido2CombinationConfiguration":
				from .fido2_combination_configuration import Fido2CombinationConfiguration
				return Fido2CombinationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.x509CertificateCombinationConfiguration":
				from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration
				return X509CertificateCombinationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationContextClassReference":
				from .authentication_context_class_reference import AuthenticationContextClassReference
				return AuthenticationContextClassReference.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationEventListener":
				from .authentication_event_listener import AuthenticationEventListener
				return AuthenticationEventListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onAttributeCollectionListener":
				from .on_attribute_collection_listener import OnAttributeCollectionListener
				return OnAttributeCollectionListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onAttributeCollectionStartListener":
				from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener
				return OnAttributeCollectionStartListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onAttributeCollectionSubmitListener":
				from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener
				return OnAttributeCollectionSubmitListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onAuthenticationMethodLoadStartListener":
				from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
				return OnAuthenticationMethodLoadStartListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onEmailOtpSendListener":
				from .on_email_otp_send_listener import OnEmailOtpSendListener
				return OnEmailOtpSendListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onInteractiveAuthFlowStartListener":
				from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
				return OnInteractiveAuthFlowStartListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onPhoneMethodLoadStartListener":
				from .on_phone_method_load_start_listener import OnPhoneMethodLoadStartListener
				return OnPhoneMethodLoadStartListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onTokenIssuanceStartListener":
				from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
				return OnTokenIssuanceStartListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onUserCreateStartListener":
				from .on_user_create_start_listener import OnUserCreateStartListener
				return OnUserCreateStartListener.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationEventsFlow":
				from .authentication_events_flow import AuthenticationEventsFlow
				return AuthenticationEventsFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.externalUsersSelfServiceSignUpEventsFlow":
				from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow
				return ExternalUsersSelfServiceSignUpEventsFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationEventsPolicy":
				from .authentication_events_policy import AuthenticationEventsPolicy
				return AuthenticationEventsPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationFailure":
				from .authentication_failure import AuthenticationFailure
				return AuthenticationFailure.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationFlowsPolicy":
				from .authentication_flows_policy import AuthenticationFlowsPolicy
				return AuthenticationFlowsPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationListener":
				from .authentication_listener import AuthenticationListener
				return AuthenticationListener.model_validate(data)
			if mapping_key == "#microsoft.graph.invokeUserFlowListener":
				from .invoke_user_flow_listener import InvokeUserFlowListener
				return InvokeUserFlowListener.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationMethod":
				from .authentication_method import AuthenticationMethod
				return AuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.emailAuthenticationMethod":
				from .email_authentication_method import EmailAuthenticationMethod
				return EmailAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.fido2AuthenticationMethod":
				from .fido2_authentication_method import Fido2AuthenticationMethod
				return Fido2AuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.hardwareOathAuthenticationMethod":
				from .hardware_oath_authentication_method import HardwareOathAuthenticationMethod
				return HardwareOathAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod":
				from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
				return MicrosoftAuthenticatorAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.passwordAuthenticationMethod":
				from .password_authentication_method import PasswordAuthenticationMethod
				return PasswordAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.passwordlessMicrosoftAuthenticatorAuthenticationMethod":
				from .passwordless_microsoft_authenticator_authentication_method import PasswordlessMicrosoftAuthenticatorAuthenticationMethod
				return PasswordlessMicrosoftAuthenticatorAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.phoneAuthenticationMethod":
				from .phone_authentication_method import PhoneAuthenticationMethod
				return PhoneAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.platformCredentialAuthenticationMethod":
				from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
				return PlatformCredentialAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.softwareOathAuthenticationMethod":
				from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
				return SoftwareOathAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.temporaryAccessPassAuthenticationMethod":
				from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
				return TemporaryAccessPassAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsHelloForBusinessAuthenticationMethod":
				from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod
				return WindowsHelloForBusinessAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationMethodConfiguration":
				from .authentication_method_configuration import AuthenticationMethodConfiguration
				return AuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.emailAuthenticationMethodConfiguration":
				from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration
				return EmailAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.externalAuthenticationMethodConfiguration":
				from .external_authentication_method_configuration import ExternalAuthenticationMethodConfiguration
				return ExternalAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.fido2AuthenticationMethodConfiguration":
				from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
				return Fido2AuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.hardwareOathAuthenticationMethodConfiguration":
				from .hardware_oath_authentication_method_configuration import HardwareOathAuthenticationMethodConfiguration
				return HardwareOathAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodConfiguration":
				from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration
				return MicrosoftAuthenticatorAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.smsAuthenticationMethodConfiguration":
				from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration
				return SmsAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.softwareOathAuthenticationMethodConfiguration":
				from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration
				return SoftwareOathAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration":
				from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration
				return TemporaryAccessPassAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.voiceAuthenticationMethodConfiguration":
				from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration
				return VoiceAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration":
				from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration
				return X509CertificateAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationMethodDevice":
				from .authentication_method_device import AuthenticationMethodDevice
				return AuthenticationMethodDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.hardwareOathTokenAuthenticationMethodDevice":
				from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice
				return HardwareOathTokenAuthenticationMethodDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationMethodModeDetail":
				from .authentication_method_mode_detail import AuthenticationMethodModeDetail
				return AuthenticationMethodModeDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationMethodsPolicy":
				from .authentication_methods_policy import AuthenticationMethodsPolicy
				return AuthenticationMethodsPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationMethodsRoot":
				from .authentication_methods_root import AuthenticationMethodsRoot
				return AuthenticationMethodsRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationMethodTarget":
				from .authentication_method_target import AuthenticationMethodTarget
				return AuthenticationMethodTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget":
				from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
				return MicrosoftAuthenticatorAuthenticationMethodTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.passkeyAuthenticationMethodTarget":
				from .passkey_authentication_method_target import PasskeyAuthenticationMethodTarget
				return PasskeyAuthenticationMethodTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.smsAuthenticationMethodTarget":
				from .sms_authentication_method_target import SmsAuthenticationMethodTarget
				return SmsAuthenticationMethodTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.voiceAuthenticationMethodTarget":
				from .voice_authentication_method_target import VoiceAuthenticationMethodTarget
				return VoiceAuthenticationMethodTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationsMetric":
				from .authentications_metric import AuthenticationsMetric
				return AuthenticationsMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationStrengthPolicy":
				from .authentication_strength_policy import AuthenticationStrengthPolicy
				return AuthenticationStrengthPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationStrengthRoot":
				from .authentication_strength_root import AuthenticationStrengthRoot
				return AuthenticationStrengthRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.authoredNote":
				from .authored_note import AuthoredNote
				return AuthoredNote.model_validate(data)
			if mapping_key == "#microsoft.graph.authorizationSystem":
				from .authorization_system import AuthorizationSystem
				return AuthorizationSystem.model_validate(data)
			if mapping_key == "#microsoft.graph.awsAuthorizationSystem":
				from .aws_authorization_system import AwsAuthorizationSystem
				return AwsAuthorizationSystem.model_validate(data)
			if mapping_key == "#microsoft.graph.azureAuthorizationSystem":
				from .azure_authorization_system import AzureAuthorizationSystem
				return AzureAuthorizationSystem.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpAuthorizationSystem":
				from .gcp_authorization_system import GcpAuthorizationSystem
				return GcpAuthorizationSystem.model_validate(data)
			if mapping_key == "#microsoft.graph.authorizationSystemIdentity":
				from .authorization_system_identity import AuthorizationSystemIdentity
				return AuthorizationSystemIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.awsIdentity":
				from .aws_identity import AwsIdentity
				return AwsIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.awsAccessKey":
				from .aws_access_key import AwsAccessKey
				return AwsAccessKey.model_validate(data)
			if mapping_key == "#microsoft.graph.awsEc2Instance":
				from .aws_ec2_instance import AwsEc2Instance
				return AwsEc2Instance.model_validate(data)
			if mapping_key == "#microsoft.graph.awsGroup":
				from .aws_group import AwsGroup
				return AwsGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.awsLambda":
				from .aws_lambda import AwsLambda
				return AwsLambda.model_validate(data)
			if mapping_key == "#microsoft.graph.awsRole":
				from .aws_role import AwsRole
				return AwsRole.model_validate(data)
			if mapping_key == "#microsoft.graph.awsUser":
				from .aws_user import AwsUser
				return AwsUser.model_validate(data)
			if mapping_key == "#microsoft.graph.azureIdentity":
				from .azure_identity import AzureIdentity
				return AzureIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.azureGroup":
				from .azure_group import AzureGroup
				return AzureGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.azureManagedIdentity":
				from .azure_managed_identity import AzureManagedIdentity
				return AzureManagedIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.azureServerlessFunction":
				from .azure_serverless_function import AzureServerlessFunction
				return AzureServerlessFunction.model_validate(data)
			if mapping_key == "#microsoft.graph.azureServicePrincipal":
				from .azure_service_principal import AzureServicePrincipal
				return AzureServicePrincipal.model_validate(data)
			if mapping_key == "#microsoft.graph.azureUser":
				from .azure_user import AzureUser
				return AzureUser.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpIdentity":
				from .gcp_identity import GcpIdentity
				return GcpIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpCloudFunction":
				from .gcp_cloud_function import GcpCloudFunction
				return GcpCloudFunction.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpGroup":
				from .gcp_group import GcpGroup
				return GcpGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpServiceAccount":
				from .gcp_service_account import GcpServiceAccount
				return GcpServiceAccount.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpUser":
				from .gcp_user import GcpUser
				return GcpUser.model_validate(data)
			if mapping_key == "#microsoft.graph.authorizationSystemResource":
				from .authorization_system_resource import AuthorizationSystemResource
				return AuthorizationSystemResource.model_validate(data)
			if mapping_key == "#microsoft.graph.awsAuthorizationSystemResource":
				from .aws_authorization_system_resource import AwsAuthorizationSystemResource
				return AwsAuthorizationSystemResource.model_validate(data)
			if mapping_key == "#microsoft.graph.azureAuthorizationSystemResource":
				from .azure_authorization_system_resource import AzureAuthorizationSystemResource
				return AzureAuthorizationSystemResource.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpAuthorizationSystemResource":
				from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
				return GcpAuthorizationSystemResource.model_validate(data)
			if mapping_key == "#microsoft.graph.authorizationSystemTypeAction":
				from .authorization_system_type_action import AuthorizationSystemTypeAction
				return AuthorizationSystemTypeAction.model_validate(data)
			if mapping_key == "#microsoft.graph.awsAuthorizationSystemTypeAction":
				from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction
				return AwsAuthorizationSystemTypeAction.model_validate(data)
			if mapping_key == "#microsoft.graph.azureAuthorizationSystemTypeAction":
				from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction
				return AzureAuthorizationSystemTypeAction.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpAuthorizationSystemTypeAction":
				from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
				return GcpAuthorizationSystemTypeAction.model_validate(data)
			if mapping_key == "#microsoft.graph.authorizationSystemTypeService":
				from .authorization_system_type_service import AuthorizationSystemTypeService
				return AuthorizationSystemTypeService.model_validate(data)
			if mapping_key == "#microsoft.graph.awsPolicy":
				from .aws_policy import AwsPolicy
				return AwsPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.azureADAuthentication":
				from .azure_a_d_authentication import AzureADAuthentication
				return AzureADAuthentication.model_validate(data)
			if mapping_key == "#microsoft.graph.azureRoleDefinition":
				from .azure_role_definition import AzureRoleDefinition
				return AzureRoleDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.b2cAuthenticationMethodsPolicy":
				from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicy
				return B2cAuthenticationMethodsPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.backupRestoreRoot":
				from .backup_restore_root import BackupRestoreRoot
				return BackupRestoreRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.baseItem":
				from .base_item import BaseItem
				return BaseItem.model_validate(data)
			if mapping_key == "#microsoft.graph.baseSitePage":
				from .base_site_page import BaseSitePage
				return BaseSitePage.model_validate(data)
			if mapping_key == "#microsoft.graph.newsLinkPage":
				from .news_link_page import NewsLinkPage
				return NewsLinkPage.model_validate(data)
			if mapping_key == "#microsoft.graph.pageTemplate":
				from .page_template import PageTemplate
				return PageTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.sitePage":
				from .site_page import SitePage
				return SitePage.model_validate(data)
			if mapping_key == "#microsoft.graph.videoNewsLinkPage":
				from .video_news_link_page import VideoNewsLinkPage
				return VideoNewsLinkPage.model_validate(data)
			if mapping_key == "#microsoft.graph.drive":
				from .drive import Drive
				return Drive.model_validate(data)
			if mapping_key == "#microsoft.graph.driveItem":
				from .drive_item import DriveItem
				return DriveItem.model_validate(data)
			if mapping_key == "#microsoft.graph.list":
				from .list import List
				return List.model_validate(data)
			if mapping_key == "#microsoft.graph.listItem":
				from .list_item import ListItem
				return ListItem.model_validate(data)
			if mapping_key == "#microsoft.graph.recycleBin":
				from .recycle_bin import RecycleBin
				return RecycleBin.model_validate(data)
			if mapping_key == "#microsoft.graph.recycleBinItem":
				from .recycle_bin_item import RecycleBinItem
				return RecycleBinItem.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedDriveItem":
				from .shared_drive_item import SharedDriveItem
				return SharedDriveItem.model_validate(data)
			if mapping_key == "#microsoft.graph.site":
				from .site import Site
				return Site.model_validate(data)
			if mapping_key == "#microsoft.graph.baseItemVersion":
				from .base_item_version import BaseItemVersion
				return BaseItemVersion.model_validate(data)
			if mapping_key == "#microsoft.graph.driveItemVersion":
				from .drive_item_version import DriveItemVersion
				return DriveItemVersion.model_validate(data)
			if mapping_key == "#microsoft.graph.listItemVersion":
				from .list_item_version import ListItemVersion
				return ListItemVersion.model_validate(data)
			if mapping_key == "#microsoft.graph.documentSetVersion":
				from .document_set_version import DocumentSetVersion
				return DocumentSetVersion.model_validate(data)
			if mapping_key == "#microsoft.graph.bitlocker":
				from .bitlocker import Bitlocker
				return Bitlocker.model_validate(data)
			if mapping_key == "#microsoft.graph.bitlockerRecoveryKey":
				from .bitlocker_recovery_key import BitlockerRecoveryKey
				return BitlockerRecoveryKey.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingAppointment":
				from .booking_appointment import BookingAppointment
				return BookingAppointment.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingCurrency":
				from .booking_currency import BookingCurrency
				return BookingCurrency.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingCustomQuestion":
				from .booking_custom_question import BookingCustomQuestion
				return BookingCustomQuestion.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingNamedEntity":
				from .booking_named_entity import BookingNamedEntity
				return BookingNamedEntity.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingBusiness":
				from .booking_business import BookingBusiness
				return BookingBusiness.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingPerson":
				from .booking_person import BookingPerson
				return BookingPerson.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingCustomer":
				from .booking_customer import BookingCustomer
				return BookingCustomer.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingStaffMember":
				from .booking_staff_member import BookingStaffMember
				return BookingStaffMember.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingService":
				from .booking_service import BookingService
				return BookingService.model_validate(data)
			if mapping_key == "#microsoft.graph.browserSharedCookie":
				from .browser_shared_cookie import BrowserSharedCookie
				return BrowserSharedCookie.model_validate(data)
			if mapping_key == "#microsoft.graph.browserSite":
				from .browser_site import BrowserSite
				return BrowserSite.model_validate(data)
			if mapping_key == "#microsoft.graph.browserSiteList":
				from .browser_site_list import BrowserSiteList
				return BrowserSiteList.model_validate(data)
			if mapping_key == "#microsoft.graph.bulkUpload":
				from .bulk_upload import BulkUpload
				return BulkUpload.model_validate(data)
			if mapping_key == "#microsoft.graph.businessFlow":
				from .business_flow import BusinessFlow
				return BusinessFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.businessFlowTemplate":
				from .business_flow_template import BusinessFlowTemplate
				return BusinessFlowTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.businessScenario":
				from .business_scenario import BusinessScenario
				return BusinessScenario.model_validate(data)
			if mapping_key == "#microsoft.graph.businessScenarioPlanner":
				from .business_scenario_planner import BusinessScenarioPlanner
				return BusinessScenarioPlanner.model_validate(data)
			if mapping_key == "#microsoft.graph.businessScenarioPlanReference":
				from .business_scenario_plan_reference import BusinessScenarioPlanReference
				return BusinessScenarioPlanReference.model_validate(data)
			if mapping_key == "#microsoft.graph.calendar":
				from .calendar import Calendar
				return Calendar.model_validate(data)
			if mapping_key == "#microsoft.graph.calendarGroup":
				from .calendar_group import CalendarGroup
				return CalendarGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.calendarPermission":
				from .calendar_permission import CalendarPermission
				return CalendarPermission.model_validate(data)
			if mapping_key == "#microsoft.graph.call":
				from .call import Call
				return Call.model_validate(data)
			if mapping_key == "#microsoft.graph.callAiInsight":
				from .call_ai_insight import CallAiInsight
				return CallAiInsight.model_validate(data)
			if mapping_key == "#microsoft.graph.callEvent":
				from .call_event import CallEvent
				return CallEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.emergencyCallEvent":
				from .emergency_call_event import EmergencyCallEvent
				return EmergencyCallEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecording":
				from .call_recording import CallRecording
				return CallRecording.model_validate(data)
			if mapping_key == "#microsoft.graph.callSettings":
				from .call_settings import CallSettings
				return CallSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.callTranscript":
				from .call_transcript import CallTranscript
				return CallTranscript.model_validate(data)
			if mapping_key == "#microsoft.graph.canvasLayout":
				from .canvas_layout import CanvasLayout
				return CanvasLayout.model_validate(data)
			if mapping_key == "#microsoft.graph.cartToClassAssociation":
				from .cart_to_class_association import CartToClassAssociation
				return CartToClassAssociation.model_validate(data)
			if mapping_key == "#microsoft.graph.certificateAuthorityAsEntity":
				from .certificate_authority_as_entity import CertificateAuthorityAsEntity
				return CertificateAuthorityAsEntity.model_validate(data)
			if mapping_key == "#microsoft.graph.certificateAuthorityPath":
				from .certificate_authority_path import CertificateAuthorityPath
				return CertificateAuthorityPath.model_validate(data)
			if mapping_key == "#microsoft.graph.certificateBasedAuthConfiguration":
				from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
				return CertificateBasedAuthConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.certificateConnectorDetails":
				from .certificate_connector_details import CertificateConnectorDetails
				return CertificateConnectorDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.changeItemBase":
				from .change_item_base import ChangeItemBase
				return ChangeItemBase.model_validate(data)
			if mapping_key == "#microsoft.graph.announcement":
				from .announcement import Announcement
				return Announcement.model_validate(data)
			if mapping_key == "#microsoft.graph.roadmap":
				from .roadmap import Roadmap
				return Roadmap.model_validate(data)
			if mapping_key == "#microsoft.graph.changeTrackedEntity":
				from .change_tracked_entity import ChangeTrackedEntity
				return ChangeTrackedEntity.model_validate(data)
			if mapping_key == "#microsoft.graph.dayNote":
				from .day_note import DayNote
				return DayNote.model_validate(data)
			if mapping_key == "#microsoft.graph.openShift":
				from .open_shift import OpenShift
				return OpenShift.model_validate(data)
			if mapping_key == "#microsoft.graph.scheduleChangeRequest":
				from .schedule_change_request import ScheduleChangeRequest
				return ScheduleChangeRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.offerShiftRequest":
				from .offer_shift_request import OfferShiftRequest
				return OfferShiftRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.swapShiftsChangeRequest":
				from .swap_shifts_change_request import SwapShiftsChangeRequest
				return SwapShiftsChangeRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.openShiftChangeRequest":
				from .open_shift_change_request import OpenShiftChangeRequest
				return OpenShiftChangeRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.timeOffRequest":
				from .time_off_request import TimeOffRequest
				return TimeOffRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.schedulingGroup":
				from .scheduling_group import SchedulingGroup
				return SchedulingGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.shift":
				from .shift import Shift
				return Shift.model_validate(data)
			if mapping_key == "#microsoft.graph.shiftPreferences":
				from .shift_preferences import ShiftPreferences
				return ShiftPreferences.model_validate(data)
			if mapping_key == "#microsoft.graph.timeCard":
				from .time_card import TimeCard
				return TimeCard.model_validate(data)
			if mapping_key == "#microsoft.graph.timeOff":
				from .time_off import TimeOff
				return TimeOff.model_validate(data)
			if mapping_key == "#microsoft.graph.timeOffReason":
				from .time_off_reason import TimeOffReason
				return TimeOffReason.model_validate(data)
			if mapping_key == "#microsoft.graph.workforceIntegration":
				from .workforce_integration import WorkforceIntegration
				return WorkforceIntegration.model_validate(data)
			if mapping_key == "#microsoft.graph.channel":
				from .channel import Channel
				return Channel.model_validate(data)
			if mapping_key == "#microsoft.graph.chat":
				from .chat import Chat
				return Chat.model_validate(data)
			if mapping_key == "#microsoft.graph.chatMessage":
				from .chat_message import ChatMessage
				return ChatMessage.model_validate(data)
			if mapping_key == "#microsoft.graph.chatMessageInfo":
				from .chat_message_info import ChatMessageInfo
				return ChatMessageInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.checklistItem":
				from .checklist_item import ChecklistItem
				return ChecklistItem.model_validate(data)
			if mapping_key == "#microsoft.graph.chromeOSOnboardingSettings":
				from .chrome_o_s_onboarding_settings import ChromeOSOnboardingSettings
				return ChromeOSOnboardingSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudAppSecurityProfile":
				from .cloud_app_security_profile import CloudAppSecurityProfile
				return CloudAppSecurityProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudCertificationAuthority":
				from .cloud_certification_authority import CloudCertificationAuthority
				return CloudCertificationAuthority.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudCertificationAuthorityLeafCertificate":
				from .cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificate
				return CloudCertificationAuthorityLeafCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudClipboardItem":
				from .cloud_clipboard_item import CloudClipboardItem
				return CloudClipboardItem.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudClipboardRoot":
				from .cloud_clipboard_root import CloudClipboardRoot
				return CloudClipboardRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPC":
				from .cloud_p_c import CloudPC
				return CloudPC.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcAuditEvent":
				from .cloud_pc_audit_event import CloudPcAuditEvent
				return CloudPcAuditEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkAction":
				from .cloud_pc_bulk_action import CloudPcBulkAction
				return CloudPcBulkAction.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkCreateSnapshot":
				from .cloud_pc_bulk_create_snapshot import CloudPcBulkCreateSnapshot
				return CloudPcBulkCreateSnapshot.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkDisasterRecoveryFailback":
				from .cloud_pc_bulk_disaster_recovery_failback import CloudPcBulkDisasterRecoveryFailback
				return CloudPcBulkDisasterRecoveryFailback.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkDisasterRecoveryFailover":
				from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover
				return CloudPcBulkDisasterRecoveryFailover.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkModifyDiskEncryptionType":
				from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType
				return CloudPcBulkModifyDiskEncryptionType.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkMove":
				from .cloud_pc_bulk_move import CloudPcBulkMove
				return CloudPcBulkMove.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkPowerOff":
				from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
				return CloudPcBulkPowerOff.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkPowerOn":
				from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
				return CloudPcBulkPowerOn.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkReprovision":
				from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
				return CloudPcBulkReprovision.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkResize":
				from .cloud_pc_bulk_resize import CloudPcBulkResize
				return CloudPcBulkResize.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkRestart":
				from .cloud_pc_bulk_restart import CloudPcBulkRestart
				return CloudPcBulkRestart.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkRestore":
				from .cloud_pc_bulk_restore import CloudPcBulkRestore
				return CloudPcBulkRestore.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkSetReviewStatus":
				from .cloud_pc_bulk_set_review_status import CloudPcBulkSetReviewStatus
				return CloudPcBulkSetReviewStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkTroubleshoot":
				from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot
				return CloudPcBulkTroubleshoot.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPCConnectivityIssue":
				from .cloud_p_c_connectivity_issue import CloudPCConnectivityIssue
				return CloudPCConnectivityIssue.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcCrossCloudGovernmentOrganizationMapping":
				from .cloud_pc_cross_cloud_government_organization_mapping import CloudPcCrossCloudGovernmentOrganizationMapping
				return CloudPcCrossCloudGovernmentOrganizationMapping.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcDeviceImage":
				from .cloud_pc_device_image import CloudPcDeviceImage
				return CloudPcDeviceImage.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcExportJob":
				from .cloud_pc_export_job import CloudPcExportJob
				return CloudPcExportJob.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcExternalPartnerSetting":
				from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting
				return CloudPcExternalPartnerSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcFrontLineServicePlan":
				from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan
				return CloudPcFrontLineServicePlan.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcGalleryImage":
				from .cloud_pc_gallery_image import CloudPcGalleryImage
				return CloudPcGalleryImage.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcOnPremisesConnection":
				from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
				return CloudPcOnPremisesConnection.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcOrganizationSettings":
				from .cloud_pc_organization_settings import CloudPcOrganizationSettings
				return CloudPcOrganizationSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcProvisioningPolicy":
				from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
				return CloudPcProvisioningPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcProvisioningPolicyAssignment":
				from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
				return CloudPcProvisioningPolicyAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcReports":
				from .cloud_pc_reports import CloudPcReports
				return CloudPcReports.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcServicePlan":
				from .cloud_pc_service_plan import CloudPcServicePlan
				return CloudPcServicePlan.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcSnapshot":
				from .cloud_pc_snapshot import CloudPcSnapshot
				return CloudPcSnapshot.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcSupportedRegion":
				from .cloud_pc_supported_region import CloudPcSupportedRegion
				return CloudPcSupportedRegion.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcUserSetting":
				from .cloud_pc_user_setting import CloudPcUserSetting
				return CloudPcUserSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcUserSettingAssignment":
				from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
				return CloudPcUserSettingAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.columnDefinition":
				from .column_definition import ColumnDefinition
				return ColumnDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.columnLink":
				from .column_link import ColumnLink
				return ColumnLink.model_validate(data)
			if mapping_key == "#microsoft.graph.comanagementEligibleDevice":
				from .comanagement_eligible_device import ComanagementEligibleDevice
				return ComanagementEligibleDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.command":
				from .command import Command
				return Command.model_validate(data)
			if mapping_key == "#microsoft.graph.commsOperation":
				from .comms_operation import CommsOperation
				return CommsOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.addLargeGalleryViewOperation":
				from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
				return AddLargeGalleryViewOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.cancelMediaProcessingOperation":
				from .cancel_media_processing_operation import CancelMediaProcessingOperation
				return CancelMediaProcessingOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.inviteParticipantsOperation":
				from .invite_participants_operation import InviteParticipantsOperation
				return InviteParticipantsOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.muteParticipantOperation":
				from .mute_participant_operation import MuteParticipantOperation
				return MuteParticipantOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.muteParticipantsOperation":
				from .mute_participants_operation import MuteParticipantsOperation
				return MuteParticipantsOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.playPromptOperation":
				from .play_prompt_operation import PlayPromptOperation
				return PlayPromptOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.recordOperation":
				from .record_operation import RecordOperation
				return RecordOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.sendDtmfTonesOperation":
				from .send_dtmf_tones_operation import SendDtmfTonesOperation
				return SendDtmfTonesOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.startHoldMusicOperation":
				from .start_hold_music_operation import StartHoldMusicOperation
				return StartHoldMusicOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.startRecordingOperation":
				from .start_recording_operation import StartRecordingOperation
				return StartRecordingOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.startTranscriptionOperation":
				from .start_transcription_operation import StartTranscriptionOperation
				return StartTranscriptionOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.stopHoldMusicOperation":
				from .stop_hold_music_operation import StopHoldMusicOperation
				return StopHoldMusicOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.stopRecordingOperation":
				from .stop_recording_operation import StopRecordingOperation
				return StopRecordingOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.stopTranscriptionOperation":
				from .stop_transcription_operation import StopTranscriptionOperation
				return StopTranscriptionOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.subscribeToToneOperation":
				from .subscribe_to_tone_operation import SubscribeToToneOperation
				return SubscribeToToneOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.unmuteParticipantOperation":
				from .unmute_participant_operation import UnmuteParticipantOperation
				return UnmuteParticipantOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.updateRecordingStatusOperation":
				from .update_recording_status_operation import UpdateRecordingStatusOperation
				return UpdateRecordingStatusOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.community":
				from .community import Community
				return Community.model_validate(data)
			if mapping_key == "#microsoft.graph.companySubscription":
				from .company_subscription import CompanySubscription
				return CompanySubscription.model_validate(data)
			if mapping_key == "#microsoft.graph.complianceManagementPartner":
				from .compliance_management_partner import ComplianceManagementPartner
				return ComplianceManagementPartner.model_validate(data)
			if mapping_key == "#microsoft.graph.conditionalAccessPolicy":
				from .conditional_access_policy import ConditionalAccessPolicy
				return ConditionalAccessPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.conditionalAccessWhatIfPolicy":
				from .conditional_access_what_if_policy import ConditionalAccessWhatIfPolicy
				return ConditionalAccessWhatIfPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.conditionalAccessRoot":
				from .conditional_access_root import ConditionalAccessRoot
				return ConditionalAccessRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.conditionalAccessTemplate":
				from .conditional_access_template import ConditionalAccessTemplate
				return ConditionalAccessTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.configManagerCollection":
				from .config_manager_collection import ConfigManagerCollection
				return ConfigManagerCollection.model_validate(data)
			if mapping_key == "#microsoft.graph.connectedOrganization":
				from .connected_organization import ConnectedOrganization
				return ConnectedOrganization.model_validate(data)
			if mapping_key == "#microsoft.graph.connectionOperation":
				from .connection_operation import ConnectionOperation
				return ConnectionOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.connector":
				from .connector import Connector
				return Connector.model_validate(data)
			if mapping_key == "#microsoft.graph.connectorGroup":
				from .connector_group import ConnectorGroup
				return ConnectorGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.contactFolder":
				from .contact_folder import ContactFolder
				return ContactFolder.model_validate(data)
			if mapping_key == "#microsoft.graph.contactMergeSuggestions":
				from .contact_merge_suggestions import ContactMergeSuggestions
				return ContactMergeSuggestions.model_validate(data)
			if mapping_key == "#microsoft.graph.contentModel":
				from .content_model import ContentModel
				return ContentModel.model_validate(data)
			if mapping_key == "#microsoft.graph.contentSharingSession":
				from .content_sharing_session import ContentSharingSession
				return ContentSharingSession.model_validate(data)
			if mapping_key == "#microsoft.graph.contentType":
				from .content_type import ContentType
				return ContentType.model_validate(data)
			if mapping_key == "#microsoft.graph.continuousAccessEvaluationPolicy":
				from .continuous_access_evaluation_policy import ContinuousAccessEvaluationPolicy
				return ContinuousAccessEvaluationPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.conversation":
				from .conversation import Conversation
				return Conversation.model_validate(data)
			if mapping_key == "#microsoft.graph.conversationMember":
				from .conversation_member import ConversationMember
				return ConversationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.aadUserConversationMember":
				from .aad_user_conversation_member import AadUserConversationMember
				return AadUserConversationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.anonymousGuestConversationMember":
				from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
				return AnonymousGuestConversationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.azureCommunicationServicesUserConversationMember":
				from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
				return AzureCommunicationServicesUserConversationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftAccountUserConversationMember":
				from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
				return MicrosoftAccountUserConversationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.skypeForBusinessUserConversationMember":
				from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
				return SkypeForBusinessUserConversationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.skypeUserConversationMember":
				from .skype_user_conversation_member import SkypeUserConversationMember
				return SkypeUserConversationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.conversationThread":
				from .conversation_thread import ConversationThread
				return ConversationThread.model_validate(data)
			if mapping_key == "#microsoft.graph.copilotAdmin":
				from .copilot_admin import CopilotAdmin
				return CopilotAdmin.model_validate(data)
			if mapping_key == "#microsoft.graph.copilotAdminLimitedMode":
				from .copilot_admin_limited_mode import CopilotAdminLimitedMode
				return CopilotAdminLimitedMode.model_validate(data)
			if mapping_key == "#microsoft.graph.copilotAdminSetting":
				from .copilot_admin_setting import CopilotAdminSetting
				return CopilotAdminSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.corsConfiguration_v2":
				from .cors_configuration_v2 import CorsConfiguration_v2
				return CorsConfiguration_v2.model_validate(data)
			if mapping_key == "#microsoft.graph.credentialUsageSummary":
				from .credential_usage_summary import CredentialUsageSummary
				return CredentialUsageSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.credentialUserRegistrationCount":
				from .credential_user_registration_count import CredentialUserRegistrationCount
				return CredentialUserRegistrationCount.model_validate(data)
			if mapping_key == "#microsoft.graph.credentialUserRegistrationDetails":
				from .credential_user_registration_details import CredentialUserRegistrationDetails
				return CredentialUserRegistrationDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.crossTenantAccessPolicyConfigurationDefault":
				from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
				return CrossTenantAccessPolicyConfigurationDefault.model_validate(data)
			if mapping_key == "#microsoft.graph.customCalloutExtension":
				from .custom_callout_extension import CustomCalloutExtension
				return CustomCalloutExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageAssignmentRequestWorkflowExtension":
				from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
				return AccessPackageAssignmentRequestWorkflowExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageAssignmentWorkflowExtension":
				from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
				return AccessPackageAssignmentWorkflowExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.customAccessPackageWorkflowExtension":
				from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
				return CustomAccessPackageWorkflowExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.customAuthenticationExtension":
				from .custom_authentication_extension import CustomAuthenticationExtension
				return CustomAuthenticationExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.onAttributeCollectionStartCustomExtension":
				from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
				return OnAttributeCollectionStartCustomExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.onAttributeCollectionSubmitCustomExtension":
				from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
				return OnAttributeCollectionSubmitCustomExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.onOtpSendCustomExtension":
				from .on_otp_send_custom_extension import OnOtpSendCustomExtension
				return OnOtpSendCustomExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.onTokenIssuanceStartCustomExtension":
				from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
				return OnTokenIssuanceStartCustomExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.customTaskExtension":
				from .identity_governance_custom_task_extension import IdentityGovernanceCustomTaskExtension
				return IdentityGovernanceCustomTaskExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.customClaimsPolicy":
				from .custom_claims_policy import CustomClaimsPolicy
				return CustomClaimsPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.customExtensionHandler":
				from .custom_extension_handler import CustomExtensionHandler
				return CustomExtensionHandler.model_validate(data)
			if mapping_key == "#microsoft.graph.customExtensionStageSetting":
				from .custom_extension_stage_setting import CustomExtensionStageSetting
				return CustomExtensionStageSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.customSecurityAttributeAudit":
				from .custom_security_attribute_audit import CustomSecurityAttributeAudit
				return CustomSecurityAttributeAudit.model_validate(data)
			if mapping_key == "#microsoft.graph.customSecurityAttributeDefinition":
				from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
				return CustomSecurityAttributeDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.customSecurityAttributeExemption":
				from .custom_security_attribute_exemption import CustomSecurityAttributeExemption
				return CustomSecurityAttributeExemption.model_validate(data)
			if mapping_key == "#microsoft.graph.customSecurityAttributeStringValueExemption":
				from .custom_security_attribute_string_value_exemption import CustomSecurityAttributeStringValueExemption
				return CustomSecurityAttributeStringValueExemption.model_validate(data)
			if mapping_key == "#microsoft.graph.dailyUserInsightMetricsRoot":
				from .daily_user_insight_metrics_root import DailyUserInsightMetricsRoot
				return DailyUserInsightMetricsRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.dataClassificationService":
				from .data_classification_service import DataClassificationService
				return DataClassificationService.model_validate(data)
			if mapping_key == "#microsoft.graph.dataCollectionInfo":
				from .data_collection_info import DataCollectionInfo
				return DataCollectionInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.dataLossPreventionPolicy":
				from .data_loss_prevention_policy import DataLossPreventionPolicy
				return DataLossPreventionPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.dataPolicyOperation":
				from .data_policy_operation import DataPolicyOperation
				return DataPolicyOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.dataSharingConsent":
				from .data_sharing_consent import DataSharingConsent
				return DataSharingConsent.model_validate(data)
			if mapping_key == "#microsoft.graph.defaultUserRoleOverride":
				from .default_user_role_override import DefaultUserRoleOverride
				return DefaultUserRoleOverride.model_validate(data)
			if mapping_key == "#microsoft.graph.delegatedAdminAccessAssignment":
				from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
				return DelegatedAdminAccessAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.delegatedAdminCustomer":
				from .delegated_admin_customer import DelegatedAdminCustomer
				return DelegatedAdminCustomer.model_validate(data)
			if mapping_key == "#microsoft.graph.delegatedAdminRelationship":
				from .delegated_admin_relationship import DelegatedAdminRelationship
				return DelegatedAdminRelationship.model_validate(data)
			if mapping_key == "#microsoft.graph.resellerDelegatedAdminRelationship":
				from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship
				return ResellerDelegatedAdminRelationship.model_validate(data)
			if mapping_key == "#microsoft.graph.delegatedAdminRelationshipOperation":
				from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
				return DelegatedAdminRelationshipOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.delegatedAdminRelationshipRequest":
				from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest
				return DelegatedAdminRelationshipRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.delegatedAdminServiceManagementDetail":
				from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail
				return DelegatedAdminServiceManagementDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.delegatedPermissionClassification":
				from .delegated_permission_classification import DelegatedPermissionClassification
				return DelegatedPermissionClassification.model_validate(data)
			if mapping_key == "#microsoft.graph.delegationSettings":
				from .delegation_settings import DelegationSettings
				return DelegationSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.deletedChat":
				from .deleted_chat import DeletedChat
				return DeletedChat.model_validate(data)
			if mapping_key == "#microsoft.graph.deletedItemContainer":
				from .deleted_item_container import DeletedItemContainer
				return DeletedItemContainer.model_validate(data)
			if mapping_key == "#microsoft.graph.deletedTeam":
				from .deleted_team import DeletedTeam
				return DeletedTeam.model_validate(data)
			if mapping_key == "#microsoft.graph.deltaParticipants":
				from .delta_participants import DeltaParticipants
				return DeltaParticipants.model_validate(data)
			if mapping_key == "#microsoft.graph.depOnboardingSetting":
				from .dep_onboarding_setting import DepOnboardingSetting
				return DepOnboardingSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.detectedApp":
				from .detected_app import DetectedApp
				return DetectedApp.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceAndAppManagementAssignmentFilter":
				from .device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter
				return DeviceAndAppManagementAssignmentFilter.model_validate(data)
			if mapping_key == "#microsoft.graph.payloadCompatibleAssignmentFilter":
				from .payload_compatible_assignment_filter import PayloadCompatibleAssignmentFilter
				return PayloadCompatibleAssignmentFilter.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceAppManagement":
				from .device_app_management import DeviceAppManagement
				return DeviceAppManagement.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceAppManagementTask":
				from .device_app_management_task import DeviceAppManagementTask
				return DeviceAppManagementTask.model_validate(data)
			if mapping_key == "#microsoft.graph.appVulnerabilityTask":
				from .app_vulnerability_task import AppVulnerabilityTask
				return AppVulnerabilityTask.model_validate(data)
			if mapping_key == "#microsoft.graph.securityConfigurationTask":
				from .security_configuration_task import SecurityConfigurationTask
				return SecurityConfigurationTask.model_validate(data)
			if mapping_key == "#microsoft.graph.unmanagedDeviceDiscoveryTask":
				from .unmanaged_device_discovery_task import UnmanagedDeviceDiscoveryTask
				return UnmanagedDeviceDiscoveryTask.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceCategory":
				from .device_category import DeviceCategory
				return DeviceCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceComplianceActionItem":
				from .device_compliance_action_item import DeviceComplianceActionItem
				return DeviceComplianceActionItem.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceComplianceDeviceOverview":
				from .device_compliance_device_overview import DeviceComplianceDeviceOverview
				return DeviceComplianceDeviceOverview.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceComplianceDeviceStatus":
				from .device_compliance_device_status import DeviceComplianceDeviceStatus
				return DeviceComplianceDeviceStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceCompliancePolicy":
				from .device_compliance_policy import DeviceCompliancePolicy
				return DeviceCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.androidCompliancePolicy":
				from .android_compliance_policy import AndroidCompliancePolicy
				return AndroidCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerCompliancePolicy":
				from .android_device_owner_compliance_policy import AndroidDeviceOwnerCompliancePolicy
				return AndroidDeviceOwnerCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkCompliancePolicy":
				from .android_for_work_compliance_policy import AndroidForWorkCompliancePolicy
				return AndroidForWorkCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileCompliancePolicy":
				from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
				return AndroidWorkProfileCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerCompliancePolicy":
				from .aosp_device_owner_compliance_policy import AospDeviceOwnerCompliancePolicy
				return AospDeviceOwnerCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.defaultDeviceCompliancePolicy":
				from .default_device_compliance_policy import DefaultDeviceCompliancePolicy
				return DefaultDeviceCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.iosCompliancePolicy":
				from .ios_compliance_policy import IosCompliancePolicy
				return IosCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSCompliancePolicy":
				from .mac_o_s_compliance_policy import MacOSCompliancePolicy
				return MacOSCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10CompliancePolicy":
				from .windows10_compliance_policy import Windows10CompliancePolicy
				return Windows10CompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10MobileCompliancePolicy":
				from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
				return Windows10MobileCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81CompliancePolicy":
				from .windows81_compliance_policy import Windows81CompliancePolicy
				return Windows81CompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81CompliancePolicy":
				from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy
				return WindowsPhone81CompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceCompliancePolicyAssignment":
				from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
				return DeviceCompliancePolicyAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceCompliancePolicyDeviceStateSummary":
				from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
				return DeviceCompliancePolicyDeviceStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceCompliancePolicyGroupAssignment":
				from .device_compliance_policy_group_assignment import DeviceCompliancePolicyGroupAssignment
				return DeviceCompliancePolicyGroupAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceCompliancePolicySettingStateSummary":
				from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
				return DeviceCompliancePolicySettingStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceCompliancePolicyState":
				from .device_compliance_policy_state import DeviceCompliancePolicyState
				return DeviceCompliancePolicyState.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceComplianceScheduledActionForRule":
				from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
				return DeviceComplianceScheduledActionForRule.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceComplianceScript":
				from .device_compliance_script import DeviceComplianceScript
				return DeviceComplianceScript.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceComplianceScriptDeviceState":
				from .device_compliance_script_device_state import DeviceComplianceScriptDeviceState
				return DeviceComplianceScriptDeviceState.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceComplianceScriptRunSummary":
				from .device_compliance_script_run_summary import DeviceComplianceScriptRunSummary
				return DeviceComplianceScriptRunSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceComplianceSettingState":
				from .device_compliance_setting_state import DeviceComplianceSettingState
				return DeviceComplianceSettingState.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceComplianceUserOverview":
				from .device_compliance_user_overview import DeviceComplianceUserOverview
				return DeviceComplianceUserOverview.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceComplianceUserStatus":
				from .device_compliance_user_status import DeviceComplianceUserStatus
				return DeviceComplianceUserStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfiguration":
				from .device_configuration import DeviceConfiguration
				return DeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidCertificateProfileBase":
				from .android_certificate_profile_base import AndroidCertificateProfileBase
				return AndroidCertificateProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkImportedPFXCertificateProfile":
				from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
				return AndroidForWorkImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidImportedPFXCertificateProfile":
				from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
				return AndroidImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidPkcsCertificateProfile":
				from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
				return AndroidPkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidScepCertificateProfile":
				from .android_scep_certificate_profile import AndroidScepCertificateProfile
				return AndroidScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidCustomConfiguration":
				from .android_custom_configuration import AndroidCustomConfiguration
				return AndroidCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerCertificateProfileBase":
				from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
				return AndroidDeviceOwnerCertificateProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerImportedPFXCertificateProfile":
				from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile
				return AndroidDeviceOwnerImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerPkcsCertificateProfile":
				from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile
				return AndroidDeviceOwnerPkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerScepCertificateProfile":
				from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile
				return AndroidDeviceOwnerScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerDerivedCredentialAuthenticationConfiguration":
				from .android_device_owner_derived_credential_authentication_configuration import AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration
				return AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerGeneralDeviceConfiguration":
				from .android_device_owner_general_device_configuration import AndroidDeviceOwnerGeneralDeviceConfiguration
				return AndroidDeviceOwnerGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerTrustedRootCertificate":
				from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
				return AndroidDeviceOwnerTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerWiFiConfiguration":
				from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration
				return AndroidDeviceOwnerWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerEnterpriseWiFiConfiguration":
				from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
				return AndroidDeviceOwnerEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidEasEmailProfileConfiguration":
				from .android_eas_email_profile_configuration import AndroidEasEmailProfileConfiguration
				return AndroidEasEmailProfileConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkCertificateProfileBase":
				from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
				return AndroidForWorkCertificateProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkPkcsCertificateProfile":
				from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
				return AndroidForWorkPkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkScepCertificateProfile":
				from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
				return AndroidForWorkScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkCustomConfiguration":
				from .android_for_work_custom_configuration import AndroidForWorkCustomConfiguration
				return AndroidForWorkCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkEasEmailProfileBase":
				from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase
				return AndroidForWorkEasEmailProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkGmailEasConfiguration":
				from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration
				return AndroidForWorkGmailEasConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkNineWorkEasConfiguration":
				from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration
				return AndroidForWorkNineWorkEasConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkGeneralDeviceConfiguration":
				from .android_for_work_general_device_configuration import AndroidForWorkGeneralDeviceConfiguration
				return AndroidForWorkGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkTrustedRootCertificate":
				from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
				return AndroidForWorkTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkVpnConfiguration":
				from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration
				return AndroidForWorkVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkWiFiConfiguration":
				from .android_for_work_wi_fi_configuration import AndroidForWorkWiFiConfiguration
				return AndroidForWorkWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkEnterpriseWiFiConfiguration":
				from .android_for_work_enterprise_wi_fi_configuration import AndroidForWorkEnterpriseWiFiConfiguration
				return AndroidForWorkEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidGeneralDeviceConfiguration":
				from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
				return AndroidGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidOmaCpConfiguration":
				from .android_oma_cp_configuration import AndroidOmaCpConfiguration
				return AndroidOmaCpConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidTrustedRootCertificate":
				from .android_trusted_root_certificate import AndroidTrustedRootCertificate
				return AndroidTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.androidVpnConfiguration":
				from .android_vpn_configuration import AndroidVpnConfiguration
				return AndroidVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWiFiConfiguration":
				from .android_wi_fi_configuration import AndroidWiFiConfiguration
				return AndroidWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidEnterpriseWiFiConfiguration":
				from .android_enterprise_wi_fi_configuration import AndroidEnterpriseWiFiConfiguration
				return AndroidEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileCertificateProfileBase":
				from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
				return AndroidWorkProfileCertificateProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfilePkcsCertificateProfile":
				from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile
				return AndroidWorkProfilePkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileScepCertificateProfile":
				from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile
				return AndroidWorkProfileScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileCustomConfiguration":
				from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
				return AndroidWorkProfileCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileEasEmailProfileBase":
				from .android_work_profile_eas_email_profile_base import AndroidWorkProfileEasEmailProfileBase
				return AndroidWorkProfileEasEmailProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileGmailEasConfiguration":
				from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
				return AndroidWorkProfileGmailEasConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileNineWorkEasConfiguration":
				from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
				return AndroidWorkProfileNineWorkEasConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration":
				from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
				return AndroidWorkProfileGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileTrustedRootCertificate":
				from .android_work_profile_trusted_root_certificate import AndroidWorkProfileTrustedRootCertificate
				return AndroidWorkProfileTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileVpnConfiguration":
				from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration
				return AndroidWorkProfileVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileWiFiConfiguration":
				from .android_work_profile_wi_fi_configuration import AndroidWorkProfileWiFiConfiguration
				return AndroidWorkProfileWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileEnterpriseWiFiConfiguration":
				from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
				return AndroidWorkProfileEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerCertificateProfileBase":
				from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase
				return AospDeviceOwnerCertificateProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerPkcsCertificateProfile":
				from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile
				return AospDeviceOwnerPkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerScepCertificateProfile":
				from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile
				return AospDeviceOwnerScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerDeviceConfiguration":
				from .aosp_device_owner_device_configuration import AospDeviceOwnerDeviceConfiguration
				return AospDeviceOwnerDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerTrustedRootCertificate":
				from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate
				return AospDeviceOwnerTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerWiFiConfiguration":
				from .aosp_device_owner_wi_fi_configuration import AospDeviceOwnerWiFiConfiguration
				return AospDeviceOwnerWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerEnterpriseWiFiConfiguration":
				from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
				return AospDeviceOwnerEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.appleDeviceFeaturesConfigurationBase":
				from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
				return AppleDeviceFeaturesConfigurationBase.model_validate(data)
			if mapping_key == "#microsoft.graph.iosDeviceFeaturesConfiguration":
				from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
				return IosDeviceFeaturesConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSDeviceFeaturesConfiguration":
				from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
				return MacOSDeviceFeaturesConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.appleExpeditedCheckinConfigurationBase":
				from .apple_expedited_checkin_configuration_base import AppleExpeditedCheckinConfigurationBase
				return AppleExpeditedCheckinConfigurationBase.model_validate(data)
			if mapping_key == "#microsoft.graph.iosExpeditedCheckinConfiguration":
				from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration
				return IosExpeditedCheckinConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.appleVpnConfiguration":
				from .apple_vpn_configuration import AppleVpnConfiguration
				return AppleVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosVpnConfiguration":
				from .ios_vpn_configuration import IosVpnConfiguration
				return IosVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosikEv2VpnConfiguration":
				from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
				return IosikEv2VpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSVpnConfiguration":
				from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
				return MacOSVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.easEmailProfileConfigurationBase":
				from .eas_email_profile_configuration_base import EasEmailProfileConfigurationBase
				return EasEmailProfileConfigurationBase.model_validate(data)
			if mapping_key == "#microsoft.graph.iosEasEmailProfileConfiguration":
				from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
				return IosEasEmailProfileConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EasEmailProfileConfiguration":
				from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
				return Windows10EasEmailProfileConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhoneEASEmailProfileConfiguration":
				from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration
				return WindowsPhoneEASEmailProfileConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.editionUpgradeConfiguration":
				from .edition_upgrade_configuration import EditionUpgradeConfiguration
				return EditionUpgradeConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosCertificateProfile":
				from .ios_certificate_profile import IosCertificateProfile
				return IosCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.iosCertificateProfileBase":
				from .ios_certificate_profile_base import IosCertificateProfileBase
				return IosCertificateProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.iosPkcsCertificateProfile":
				from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
				return IosPkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.iosScepCertificateProfile":
				from .ios_scep_certificate_profile import IosScepCertificateProfile
				return IosScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.iosImportedPFXCertificateProfile":
				from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
				return IosImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.iosCustomConfiguration":
				from .ios_custom_configuration import IosCustomConfiguration
				return IosCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosDerivedCredentialAuthenticationConfiguration":
				from .ios_derived_credential_authentication_configuration import IosDerivedCredentialAuthenticationConfiguration
				return IosDerivedCredentialAuthenticationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosEducationDeviceConfiguration":
				from .ios_education_device_configuration import IosEducationDeviceConfiguration
				return IosEducationDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosEduDeviceConfiguration":
				from .ios_edu_device_configuration import IosEduDeviceConfiguration
				return IosEduDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosGeneralDeviceConfiguration":
				from .ios_general_device_configuration import IosGeneralDeviceConfiguration
				return IosGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosTrustedRootCertificate":
				from .ios_trusted_root_certificate import IosTrustedRootCertificate
				return IosTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.iosUpdateConfiguration":
				from .ios_update_configuration import IosUpdateConfiguration
				return IosUpdateConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosWiFiConfiguration":
				from .ios_wi_fi_configuration import IosWiFiConfiguration
				return IosWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosEnterpriseWiFiConfiguration":
				from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
				return IosEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSCertificateProfileBase":
				from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
				return MacOSCertificateProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSImportedPFXCertificateProfile":
				from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
				return MacOSImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSPkcsCertificateProfile":
				from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
				return MacOSPkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSScepCertificateProfile":
				from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
				return MacOSScepCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSCustomAppConfiguration":
				from .mac_o_s_custom_app_configuration import MacOSCustomAppConfiguration
				return MacOSCustomAppConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSCustomConfiguration":
				from .mac_o_s_custom_configuration import MacOSCustomConfiguration
				return MacOSCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSEndpointProtectionConfiguration":
				from .mac_o_s_endpoint_protection_configuration import MacOSEndpointProtectionConfiguration
				return MacOSEndpointProtectionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSExtensionsConfiguration":
				from .mac_o_s_extensions_configuration import MacOSExtensionsConfiguration
				return MacOSExtensionsConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSGeneralDeviceConfiguration":
				from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
				return MacOSGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSSoftwareUpdateConfiguration":
				from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration
				return MacOSSoftwareUpdateConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSTrustedRootCertificate":
				from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
				return MacOSTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSWiFiConfiguration":
				from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration
				return MacOSWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSEnterpriseWiFiConfiguration":
				from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
				return MacOSEnterpriseWiFiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSWiredNetworkConfiguration":
				from .mac_o_s_wired_network_configuration import MacOSWiredNetworkConfiguration
				return MacOSWiredNetworkConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedPCConfiguration":
				from .shared_p_c_configuration import SharedPCConfiguration
				return SharedPCConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.unsupportedDeviceConfiguration":
				from .unsupported_device_configuration import UnsupportedDeviceConfiguration
				return UnsupportedDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.vpnConfiguration":
				from .vpn_configuration import VpnConfiguration
				return VpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidDeviceOwnerVpnConfiguration":
				from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
				return AndroidDeviceOwnerVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10CustomConfiguration":
				from .windows10_custom_configuration import Windows10CustomConfiguration
				return Windows10CustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10DeviceFirmwareConfigurationInterface":
				from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface
				return Windows10DeviceFirmwareConfigurationInterface.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EndpointProtectionConfiguration":
				from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
				return Windows10EndpointProtectionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration":
				from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
				return Windows10EnterpriseModernAppManagementConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10GeneralConfiguration":
				from .windows10_general_configuration import Windows10GeneralConfiguration
				return Windows10GeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10NetworkBoundaryConfiguration":
				from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration
				return Windows10NetworkBoundaryConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10PFXImportCertificateProfile":
				from .windows10_p_f_x_import_certificate_profile import Windows10PFXImportCertificateProfile
				return Windows10PFXImportCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10SecureAssessmentConfiguration":
				from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
				return Windows10SecureAssessmentConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10TeamGeneralConfiguration":
				from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
				return Windows10TeamGeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81GeneralConfiguration":
				from .windows81_general_configuration import Windows81GeneralConfiguration
				return Windows81GeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81TrustedRootCertificate":
				from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
				return Windows81TrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81WifiImportConfiguration":
				from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration
				return Windows81WifiImportConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsCertificateProfileBase":
				from .windows_certificate_profile_base import WindowsCertificateProfileBase
				return WindowsCertificateProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10CertificateProfileBase":
				from .windows10_certificate_profile_base import Windows10CertificateProfileBase
				return Windows10CertificateProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10PkcsCertificateProfile":
				from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
				return Windows10PkcsCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10ImportedPFXCertificateProfile":
				from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
				return Windows10ImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81CertificateProfileBase":
				from .windows81_certificate_profile_base import Windows81CertificateProfileBase
				return Windows81CertificateProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81SCEPCertificateProfile":
				from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
				return Windows81SCEPCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81ImportedPFXCertificateProfile":
				from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
				return WindowsPhone81ImportedPFXCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration":
				from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
				return WindowsDefenderAdvancedThreatProtectionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDeliveryOptimizationConfiguration":
				from .windows_delivery_optimization_configuration import WindowsDeliveryOptimizationConfiguration
				return WindowsDeliveryOptimizationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDomainJoinConfiguration":
				from .windows_domain_join_configuration import WindowsDomainJoinConfiguration
				return WindowsDomainJoinConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsHealthMonitoringConfiguration":
				from .windows_health_monitoring_configuration import WindowsHealthMonitoringConfiguration
				return WindowsHealthMonitoringConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsIdentityProtectionConfiguration":
				from .windows_identity_protection_configuration import WindowsIdentityProtectionConfiguration
				return WindowsIdentityProtectionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsKioskConfiguration":
				from .windows_kiosk_configuration import WindowsKioskConfiguration
				return WindowsKioskConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81CertificateProfileBase":
				from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
				return WindowsPhone81CertificateProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81SCEPCertificateProfile":
				from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile
				return WindowsPhone81SCEPCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81CustomConfiguration":
				from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
				return WindowsPhone81CustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81GeneralConfiguration":
				from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
				return WindowsPhone81GeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81TrustedRootCertificate":
				from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate
				return WindowsPhone81TrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdateForBusinessConfiguration":
				from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
				return WindowsUpdateForBusinessConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsVpnConfiguration":
				from .windows_vpn_configuration import WindowsVpnConfiguration
				return WindowsVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10VpnConfiguration":
				from .windows10_vpn_configuration import Windows10VpnConfiguration
				return Windows10VpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81VpnConfiguration":
				from .windows81_vpn_configuration import Windows81VpnConfiguration
				return Windows81VpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81VpnConfiguration":
				from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
				return WindowsPhone81VpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsWifiConfiguration":
				from .windows_wifi_configuration import WindowsWifiConfiguration
				return WindowsWifiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsWifiEnterpriseEAPConfiguration":
				from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
				return WindowsWifiEnterpriseEAPConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsWiredNetworkConfiguration":
				from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration
				return WindowsWiredNetworkConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationAssignment":
				from .device_configuration_assignment import DeviceConfigurationAssignment
				return DeviceConfigurationAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationConflictSummary":
				from .device_configuration_conflict_summary import DeviceConfigurationConflictSummary
				return DeviceConfigurationConflictSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationDeviceOverview":
				from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
				return DeviceConfigurationDeviceOverview.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationDeviceStateSummary":
				from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
				return DeviceConfigurationDeviceStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationDeviceStatus":
				from .device_configuration_device_status import DeviceConfigurationDeviceStatus
				return DeviceConfigurationDeviceStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationGroupAssignment":
				from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment
				return DeviceConfigurationGroupAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationState":
				from .device_configuration_state import DeviceConfigurationState
				return DeviceConfigurationState.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationUserOverview":
				from .device_configuration_user_overview import DeviceConfigurationUserOverview
				return DeviceConfigurationUserOverview.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationUserStateSummary":
				from .device_configuration_user_state_summary import DeviceConfigurationUserStateSummary
				return DeviceConfigurationUserStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationUserStatus":
				from .device_configuration_user_status import DeviceConfigurationUserStatus
				return DeviceConfigurationUserStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceCustomAttributeShellScript":
				from .device_custom_attribute_shell_script import DeviceCustomAttributeShellScript
				return DeviceCustomAttributeShellScript.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceEnrollmentConfiguration":
				from .device_enrollment_configuration import DeviceEnrollmentConfiguration
				return DeviceEnrollmentConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceComanagementAuthorityConfiguration":
				from .device_comanagement_authority_configuration import DeviceComanagementAuthorityConfiguration
				return DeviceComanagementAuthorityConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceEnrollmentLimitConfiguration":
				from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
				return DeviceEnrollmentLimitConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceEnrollmentNotificationConfiguration":
				from .device_enrollment_notification_configuration import DeviceEnrollmentNotificationConfiguration
				return DeviceEnrollmentNotificationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceEnrollmentPlatformRestrictionConfiguration":
				from .device_enrollment_platform_restriction_configuration import DeviceEnrollmentPlatformRestrictionConfiguration
				return DeviceEnrollmentPlatformRestrictionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration":
				from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
				return DeviceEnrollmentPlatformRestrictionsConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceEnrollmentWindowsHelloForBusinessConfiguration":
				from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
				return DeviceEnrollmentWindowsHelloForBusinessConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EnrollmentCompletionPageConfiguration":
				from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration
				return Windows10EnrollmentCompletionPageConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceHealthScript":
				from .device_health_script import DeviceHealthScript
				return DeviceHealthScript.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceHealthScriptAssignment":
				from .device_health_script_assignment import DeviceHealthScriptAssignment
				return DeviceHealthScriptAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceHealthScriptDeviceState":
				from .device_health_script_device_state import DeviceHealthScriptDeviceState
				return DeviceHealthScriptDeviceState.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceHealthScriptRunSummary":
				from .device_health_script_run_summary import DeviceHealthScriptRunSummary
				return DeviceHealthScriptRunSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceInstallState":
				from .device_install_state import DeviceInstallState
				return DeviceInstallState.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceLocalCredentialInfo":
				from .device_local_credential_info import DeviceLocalCredentialInfo
				return DeviceLocalCredentialInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceLogCollectionResponse":
				from .device_log_collection_response import DeviceLogCollectionResponse
				return DeviceLogCollectionResponse.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagement":
				from .device_management import DeviceManagement
				return DeviceManagement.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementAutopilotEvent":
				from .device_management_autopilot_event import DeviceManagementAutopilotEvent
				return DeviceManagementAutopilotEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementAutopilotPolicyStatusDetail":
				from .device_management_autopilot_policy_status_detail import DeviceManagementAutopilotPolicyStatusDetail
				return DeviceManagementAutopilotPolicyStatusDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementCachedReportConfiguration":
				from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration
				return DeviceManagementCachedReportConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementComplianceActionItem":
				from .device_management_compliance_action_item import DeviceManagementComplianceActionItem
				return DeviceManagementComplianceActionItem.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementCompliancePolicy":
				from .device_management_compliance_policy import DeviceManagementCompliancePolicy
				return DeviceManagementCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementComplianceScheduledActionForRule":
				from .device_management_compliance_scheduled_action_for_rule import DeviceManagementComplianceScheduledActionForRule
				return DeviceManagementComplianceScheduledActionForRule.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationCategory":
				from .device_management_configuration_category import DeviceManagementConfigurationCategory
				return DeviceManagementConfigurationCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationPolicy":
				from .device_management_configuration_policy import DeviceManagementConfigurationPolicy
				return DeviceManagementConfigurationPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationPolicyAssignment":
				from .device_management_configuration_policy_assignment import DeviceManagementConfigurationPolicyAssignment
				return DeviceManagementConfigurationPolicyAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationPolicyTemplate":
				from .device_management_configuration_policy_template import DeviceManagementConfigurationPolicyTemplate
				return DeviceManagementConfigurationPolicyTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSetting":
				from .device_management_configuration_setting import DeviceManagementConfigurationSetting
				return DeviceManagementConfigurationSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSettingDefinition":
				from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
				return DeviceManagementConfigurationSettingDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationChoiceSettingDefinition":
				from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition
				return DeviceManagementConfigurationChoiceSettingDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionDefinition":
				from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
				return DeviceManagementConfigurationChoiceSettingCollectionDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationRedirectSettingDefinition":
				from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
				return DeviceManagementConfigurationRedirectSettingDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSettingGroupDefinition":
				from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition
				return DeviceManagementConfigurationSettingGroupDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSettingGroupCollectionDefinition":
				from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
				return DeviceManagementConfigurationSettingGroupCollectionDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSimpleSettingDefinition":
				from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition
				return DeviceManagementConfigurationSimpleSettingDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionDefinition":
				from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
				return DeviceManagementConfigurationSimpleSettingCollectionDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSettingTemplate":
				from .device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate
				return DeviceManagementConfigurationSettingTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementDerivedCredentialSettings":
				from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
				return DeviceManagementDerivedCredentialSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementDomainJoinConnector":
				from .device_management_domain_join_connector import DeviceManagementDomainJoinConnector
				return DeviceManagementDomainJoinConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementExchangeConnector":
				from .device_management_exchange_connector import DeviceManagementExchangeConnector
				return DeviceManagementExchangeConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementExchangeOnPremisesPolicy":
				from .device_management_exchange_on_premises_policy import DeviceManagementExchangeOnPremisesPolicy
				return DeviceManagementExchangeOnPremisesPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementExportJob":
				from .device_management_export_job import DeviceManagementExportJob
				return DeviceManagementExportJob.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementIntent":
				from .device_management_intent import DeviceManagementIntent
				return DeviceManagementIntent.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementIntentAssignment":
				from .device_management_intent_assignment import DeviceManagementIntentAssignment
				return DeviceManagementIntentAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementIntentDeviceSettingStateSummary":
				from .device_management_intent_device_setting_state_summary import DeviceManagementIntentDeviceSettingStateSummary
				return DeviceManagementIntentDeviceSettingStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementIntentDeviceState":
				from .device_management_intent_device_state import DeviceManagementIntentDeviceState
				return DeviceManagementIntentDeviceState.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementIntentDeviceStateSummary":
				from .device_management_intent_device_state_summary import DeviceManagementIntentDeviceStateSummary
				return DeviceManagementIntentDeviceStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementIntentUserState":
				from .device_management_intent_user_state import DeviceManagementIntentUserState
				return DeviceManagementIntentUserState.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementIntentUserStateSummary":
				from .device_management_intent_user_state_summary import DeviceManagementIntentUserStateSummary
				return DeviceManagementIntentUserStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementPartner":
				from .device_management_partner import DeviceManagementPartner
				return DeviceManagementPartner.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementReports":
				from .device_management_reports import DeviceManagementReports
				return DeviceManagementReports.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementResourceAccessProfileAssignment":
				from .device_management_resource_access_profile_assignment import DeviceManagementResourceAccessProfileAssignment
				return DeviceManagementResourceAccessProfileAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementResourceAccessProfileBase":
				from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase
				return DeviceManagementResourceAccessProfileBase.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10XCertificateProfile":
				from .windows10_x_certificate_profile import Windows10XCertificateProfile
				return Windows10XCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10XSCEPCertificateProfile":
				from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile
				return Windows10XSCEPCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10XTrustedRootCertificate":
				from .windows10_x_trusted_root_certificate import Windows10XTrustedRootCertificate
				return Windows10XTrustedRootCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10XVpnConfiguration":
				from .windows10_x_vpn_configuration import Windows10XVpnConfiguration
				return Windows10XVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10XWifiConfiguration":
				from .windows10_x_wifi_configuration import Windows10XWifiConfiguration
				return Windows10XWifiConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementReusablePolicySetting":
				from .device_management_reusable_policy_setting import DeviceManagementReusablePolicySetting
				return DeviceManagementReusablePolicySetting.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementScript":
				from .device_management_script import DeviceManagementScript
				return DeviceManagementScript.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementScriptAssignment":
				from .device_management_script_assignment import DeviceManagementScriptAssignment
				return DeviceManagementScriptAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementScriptDeviceState":
				from .device_management_script_device_state import DeviceManagementScriptDeviceState
				return DeviceManagementScriptDeviceState.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementScriptGroupAssignment":
				from .device_management_script_group_assignment import DeviceManagementScriptGroupAssignment
				return DeviceManagementScriptGroupAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementScriptRunSummary":
				from .device_management_script_run_summary import DeviceManagementScriptRunSummary
				return DeviceManagementScriptRunSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementScriptUserState":
				from .device_management_script_user_state import DeviceManagementScriptUserState
				return DeviceManagementScriptUserState.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingCategory":
				from .device_management_setting_category import DeviceManagementSettingCategory
				return DeviceManagementSettingCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementIntentSettingCategory":
				from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory
				return DeviceManagementIntentSettingCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementTemplateSettingCategory":
				from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
				return DeviceManagementTemplateSettingCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingDefinition":
				from .device_management_setting_definition import DeviceManagementSettingDefinition
				return DeviceManagementSettingDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementAbstractComplexSettingDefinition":
				from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition
				return DeviceManagementAbstractComplexSettingDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementCollectionSettingDefinition":
				from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition
				return DeviceManagementCollectionSettingDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementComplexSettingDefinition":
				from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition
				return DeviceManagementComplexSettingDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementSettingInstance":
				from .device_management_setting_instance import DeviceManagementSettingInstance
				return DeviceManagementSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementAbstractComplexSettingInstance":
				from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
				return DeviceManagementAbstractComplexSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementBooleanSettingInstance":
				from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
				return DeviceManagementBooleanSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementCollectionSettingInstance":
				from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
				return DeviceManagementCollectionSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementComplexSettingInstance":
				from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
				return DeviceManagementComplexSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementIntegerSettingInstance":
				from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
				return DeviceManagementIntegerSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementStringSettingInstance":
				from .device_management_string_setting_instance import DeviceManagementStringSettingInstance
				return DeviceManagementStringSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementTemplate":
				from .device_management_template import DeviceManagementTemplate
				return DeviceManagementTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.securityBaselineTemplate":
				from .security_baseline_template import SecurityBaselineTemplate
				return SecurityBaselineTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementTemplateInsightsDefinition":
				from .device_management_template_insights_definition import DeviceManagementTemplateInsightsDefinition
				return DeviceManagementTemplateInsightsDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementTroubleshootingEvent":
				from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
				return DeviceManagementTroubleshootingEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.appleVppTokenTroubleshootingEvent":
				from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent
				return AppleVppTokenTroubleshootingEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.enrollmentTroubleshootingEvent":
				from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
				return EnrollmentTroubleshootingEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppTroubleshootingEvent":
				from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
				return MobileAppTroubleshootingEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceRegistrationPolicy":
				from .device_registration_policy import DeviceRegistrationPolicy
				return DeviceRegistrationPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceSetupConfiguration":
				from .device_setup_configuration import DeviceSetupConfiguration
				return DeviceSetupConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceShellScript":
				from .device_shell_script import DeviceShellScript
				return DeviceShellScript.model_validate(data)
			if mapping_key == "#microsoft.graph.directory":
				from .directory import Directory
				return Directory.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryAudit":
				from .directory_audit import DirectoryAudit
				return DirectoryAudit.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryDefinition":
				from .directory_definition import DirectoryDefinition
				return DirectoryDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryObject":
				from .directory_object import DirectoryObject
				return DirectoryObject.model_validate(data)
			if mapping_key == "#microsoft.graph.administrativeUnit":
				from .administrative_unit import AdministrativeUnit
				return AdministrativeUnit.model_validate(data)
			if mapping_key == "#microsoft.graph.application":
				from .application import Application
				return Application.model_validate(data)
			if mapping_key == "#microsoft.graph.appRoleAssignment":
				from .app_role_assignment import AppRoleAssignment
				return AppRoleAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.certificateAuthorityDetail":
				from .certificate_authority_detail import CertificateAuthorityDetail
				return CertificateAuthorityDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.certificateBasedAuthPki":
				from .certificate_based_auth_pki import CertificateBasedAuthPki
				return CertificateBasedAuthPki.model_validate(data)
			if mapping_key == "#microsoft.graph.contract":
				from .contract import Contract
				return Contract.model_validate(data)
			if mapping_key == "#microsoft.graph.device":
				from .device import Device
				return Device.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceTemplate":
				from .device_template import DeviceTemplate
				return DeviceTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryObjectPartnerReference":
				from .directory_object_partner_reference import DirectoryObjectPartnerReference
				return DirectoryObjectPartnerReference.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryRole":
				from .directory_role import DirectoryRole
				return DirectoryRole.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryRoleTemplate":
				from .directory_role_template import DirectoryRoleTemplate
				return DirectoryRoleTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.directorySettingTemplate":
				from .directory_setting_template import DirectorySettingTemplate
				return DirectorySettingTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.endpoint":
				from .endpoint import Endpoint
				return Endpoint.model_validate(data)
			if mapping_key == "#microsoft.graph.extensionProperty":
				from .extension_property import ExtensionProperty
				return ExtensionProperty.model_validate(data)
			if mapping_key == "#microsoft.graph.externalProfile":
				from .external_profile import ExternalProfile
				return ExternalProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.externalUserProfile":
				from .external_user_profile import ExternalUserProfile
				return ExternalUserProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.pendingExternalUserProfile":
				from .pending_external_user_profile import PendingExternalUserProfile
				return PendingExternalUserProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.federatedTokenValidationPolicy":
				from .federated_token_validation_policy import FederatedTokenValidationPolicy
				return FederatedTokenValidationPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.group":
				from .group import Group
				return Group.model_validate(data)
			if mapping_key == "#microsoft.graph.mailbox":
				from .mailbox import Mailbox
				return Mailbox.model_validate(data)
			if mapping_key == "#microsoft.graph.multiTenantOrganizationMember":
				from .multi_tenant_organization_member import MultiTenantOrganizationMember
				return MultiTenantOrganizationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.organization":
				from .organization import Organization
				return Organization.model_validate(data)
			if mapping_key == "#microsoft.graph.orgContact":
				from .org_contact import OrgContact
				return OrgContact.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionGrantPreApprovalPolicy":
				from .permission_grant_pre_approval_policy import PermissionGrantPreApprovalPolicy
				return PermissionGrantPreApprovalPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.policyBase":
				from .policy_base import PolicyBase
				return PolicyBase.model_validate(data)
			if mapping_key == "#microsoft.graph.appManagementPolicy":
				from .app_management_policy import AppManagementPolicy
				return AppManagementPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.authorizationPolicy":
				from .authorization_policy import AuthorizationPolicy
				return AuthorizationPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.externalIdentitiesPolicy":
				from .external_identities_policy import ExternalIdentitiesPolicy
				return ExternalIdentitiesPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy":
				from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
				return IdentitySecurityDefaultsEnforcementPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionGrantPolicy":
				from .permission_grant_policy import PermissionGrantPolicy
				return PermissionGrantPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.servicePrincipalCreationPolicy":
				from .service_principal_creation_policy import ServicePrincipalCreationPolicy
				return ServicePrincipalCreationPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.stsPolicy":
				from .sts_policy import StsPolicy
				return StsPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.activityBasedTimeoutPolicy":
				from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
				return ActivityBasedTimeoutPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.claimsMappingPolicy":
				from .claims_mapping_policy import ClaimsMappingPolicy
				return ClaimsMappingPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.homeRealmDiscoveryPolicy":
				from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
				return HomeRealmDiscoveryPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.tokenIssuancePolicy":
				from .token_issuance_policy import TokenIssuancePolicy
				return TokenIssuancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.tokenLifetimePolicy":
				from .token_lifetime_policy import TokenLifetimePolicy
				return TokenLifetimePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.tenantAppManagementPolicy":
				from .tenant_app_management_policy import TenantAppManagementPolicy
				return TenantAppManagementPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.tenantRelationshipAccessPolicyBase":
				from .tenant_relationship_access_policy_base import TenantRelationshipAccessPolicyBase
				return TenantRelationshipAccessPolicyBase.model_validate(data)
			if mapping_key == "#microsoft.graph.crossTenantAccessPolicy":
				from .cross_tenant_access_policy import CrossTenantAccessPolicy
				return CrossTenantAccessPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.resourceSpecificPermissionGrant":
				from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
				return ResourceSpecificPermissionGrant.model_validate(data)
			if mapping_key == "#microsoft.graph.servicePrincipal":
				from .service_principal import ServicePrincipal
				return ServicePrincipal.model_validate(data)
			if mapping_key == "#microsoft.graph.trustedCertificateAuthorityAsEntityBase":
				from .trusted_certificate_authority_as_entity_base import TrustedCertificateAuthorityAsEntityBase
				return TrustedCertificateAuthorityAsEntityBase.model_validate(data)
			if mapping_key == "#microsoft.graph.certificateBasedApplicationConfiguration":
				from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
				return CertificateBasedApplicationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.trustedCertificateAuthorityBase":
				from .trusted_certificate_authority_base import TrustedCertificateAuthorityBase
				return TrustedCertificateAuthorityBase.model_validate(data)
			if mapping_key == "#microsoft.graph.mutualTlsOauthConfiguration":
				from .mutual_tls_oauth_configuration import MutualTlsOauthConfiguration
				return MutualTlsOauthConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.user":
				from .user import User
				return User.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryRoleAccessReviewPolicy":
				from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicy
				return DirectoryRoleAccessReviewPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.directorySetting":
				from .directory_setting import DirectorySetting
				return DirectorySetting.model_validate(data)
			if mapping_key == "#microsoft.graph.document":
				from .document import Document
				return Document.model_validate(data)
			if mapping_key == "#microsoft.graph.documentComment":
				from .document_comment import DocumentComment
				return DocumentComment.model_validate(data)
			if mapping_key == "#microsoft.graph.documentCommentReply":
				from .document_comment_reply import DocumentCommentReply
				return DocumentCommentReply.model_validate(data)
			if mapping_key == "#microsoft.graph.documentProcessingJob":
				from .document_processing_job import DocumentProcessingJob
				return DocumentProcessingJob.model_validate(data)
			if mapping_key == "#microsoft.graph.domain":
				from .domain import Domain
				return Domain.model_validate(data)
			if mapping_key == "#microsoft.graph.domainDnsRecord":
				from .domain_dns_record import DomainDnsRecord
				return DomainDnsRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.domainDnsCnameRecord":
				from .domain_dns_cname_record import DomainDnsCnameRecord
				return DomainDnsCnameRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.domainDnsMxRecord":
				from .domain_dns_mx_record import DomainDnsMxRecord
				return DomainDnsMxRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.domainDnsSrvRecord":
				from .domain_dns_srv_record import DomainDnsSrvRecord
				return DomainDnsSrvRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.domainDnsTxtRecord":
				from .domain_dns_txt_record import DomainDnsTxtRecord
				return DomainDnsTxtRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.domainDnsUnavailableRecord":
				from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
				return DomainDnsUnavailableRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.domainSecurityProfile":
				from .domain_security_profile import DomainSecurityProfile
				return DomainSecurityProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.eBookInstallSummary":
				from .e_book_install_summary import EBookInstallSummary
				return EBookInstallSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.edge":
				from .edge import Edge
				return Edge.model_validate(data)
			if mapping_key == "#microsoft.graph.educationAssignment":
				from .education_assignment import EducationAssignment
				return EducationAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.educationAssignmentDefaults":
				from .education_assignment_defaults import EducationAssignmentDefaults
				return EducationAssignmentDefaults.model_validate(data)
			if mapping_key == "#microsoft.graph.educationAssignmentResource":
				from .education_assignment_resource import EducationAssignmentResource
				return EducationAssignmentResource.model_validate(data)
			if mapping_key == "#microsoft.graph.educationAssignmentSettings":
				from .education_assignment_settings import EducationAssignmentSettings
				return EducationAssignmentSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.educationCategory":
				from .education_category import EducationCategory
				return EducationCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.educationClass":
				from .education_class import EducationClass
				return EducationClass.model_validate(data)
			if mapping_key == "#microsoft.graph.educationGradingCategory":
				from .education_grading_category import EducationGradingCategory
				return EducationGradingCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.educationGradingScheme":
				from .education_grading_scheme import EducationGradingScheme
				return EducationGradingScheme.model_validate(data)
			if mapping_key == "#microsoft.graph.educationModule":
				from .education_module import EducationModule
				return EducationModule.model_validate(data)
			if mapping_key == "#microsoft.graph.educationModuleResource":
				from .education_module_resource import EducationModuleResource
				return EducationModuleResource.model_validate(data)
			if mapping_key == "#microsoft.graph.educationOrganization":
				from .education_organization import EducationOrganization
				return EducationOrganization.model_validate(data)
			if mapping_key == "#microsoft.graph.educationSchool":
				from .education_school import EducationSchool
				return EducationSchool.model_validate(data)
			if mapping_key == "#microsoft.graph.educationOutcome":
				from .education_outcome import EducationOutcome
				return EducationOutcome.model_validate(data)
			if mapping_key == "#microsoft.graph.educationFeedbackOutcome":
				from .education_feedback_outcome import EducationFeedbackOutcome
				return EducationFeedbackOutcome.model_validate(data)
			if mapping_key == "#microsoft.graph.educationFeedbackResourceOutcome":
				from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
				return EducationFeedbackResourceOutcome.model_validate(data)
			if mapping_key == "#microsoft.graph.educationPointsOutcome":
				from .education_points_outcome import EducationPointsOutcome
				return EducationPointsOutcome.model_validate(data)
			if mapping_key == "#microsoft.graph.educationRubricOutcome":
				from .education_rubric_outcome import EducationRubricOutcome
				return EducationRubricOutcome.model_validate(data)
			if mapping_key == "#microsoft.graph.educationRubric":
				from .education_rubric import EducationRubric
				return EducationRubric.model_validate(data)
			if mapping_key == "#microsoft.graph.educationSubmission":
				from .education_submission import EducationSubmission
				return EducationSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.educationSubmissionResource":
				from .education_submission_resource import EducationSubmissionResource
				return EducationSubmissionResource.model_validate(data)
			if mapping_key == "#microsoft.graph.educationUser":
				from .education_user import EducationUser
				return EducationUser.model_validate(data)
			if mapping_key == "#microsoft.graph.embeddedSIMActivationCodePool":
				from .embedded_s_i_m_activation_code_pool import EmbeddedSIMActivationCodePool
				return EmbeddedSIMActivationCodePool.model_validate(data)
			if mapping_key == "#microsoft.graph.embeddedSIMActivationCodePoolAssignment":
				from .embedded_s_i_m_activation_code_pool_assignment import EmbeddedSIMActivationCodePoolAssignment
				return EmbeddedSIMActivationCodePoolAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.embeddedSIMDeviceState":
				from .embedded_s_i_m_device_state import EmbeddedSIMDeviceState
				return EmbeddedSIMDeviceState.model_validate(data)
			if mapping_key == "#microsoft.graph.employeeExperienceUser":
				from .employee_experience_user import EmployeeExperienceUser
				return EmployeeExperienceUser.model_validate(data)
			if mapping_key == "#microsoft.graph.endpointPrivilegeManagementProvisioningStatus":
				from .endpoint_privilege_management_provisioning_status import EndpointPrivilegeManagementProvisioningStatus
				return EndpointPrivilegeManagementProvisioningStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.endUserNotification":
				from .end_user_notification import EndUserNotification
				return EndUserNotification.model_validate(data)
			if mapping_key == "#microsoft.graph.endUserNotificationDetail":
				from .end_user_notification_detail import EndUserNotificationDetail
				return EndUserNotificationDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.enrollmentConfigurationAssignment":
				from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
				return EnrollmentConfigurationAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.enrollmentProfile":
				from .enrollment_profile import EnrollmentProfile
				return EnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.depEnrollmentBaseProfile":
				from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
				return DepEnrollmentBaseProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.depIOSEnrollmentProfile":
				from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
				return DepIOSEnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.depMacOSEnrollmentProfile":
				from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
				return DepMacOSEnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.depEnrollmentProfile":
				from .dep_enrollment_profile import DepEnrollmentProfile
				return DepEnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.depTvOSEnrollmentProfile":
				from .dep_tv_o_s_enrollment_profile import DepTvOSEnrollmentProfile
				return DepTvOSEnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.depVisionOSEnrollmentProfile":
				from .dep_vision_o_s_enrollment_profile import DepVisionOSEnrollmentProfile
				return DepVisionOSEnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.enterpriseCodeSigningCertificate":
				from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
				return EnterpriseCodeSigningCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.entitlementManagement":
				from .entitlement_management import EntitlementManagement
				return EntitlementManagement.model_validate(data)
			if mapping_key == "#microsoft.graph.entitlementManagementSettings":
				from .entitlement_management_settings import EntitlementManagementSettings
				return EntitlementManagementSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.entra":
				from .entra import Entra
				return Entra.model_validate(data)
			if mapping_key == "#microsoft.graph.exactMatchDataStoreBase":
				from .exact_match_data_store_base import ExactMatchDataStoreBase
				return ExactMatchDataStoreBase.model_validate(data)
			if mapping_key == "#microsoft.graph.exactMatchDataStore":
				from .exact_match_data_store import ExactMatchDataStore
				return ExactMatchDataStore.model_validate(data)
			if mapping_key == "#microsoft.graph.exactMatchJobBase":
				from .exact_match_job_base import ExactMatchJobBase
				return ExactMatchJobBase.model_validate(data)
			if mapping_key == "#microsoft.graph.exactMatchLookupJob":
				from .exact_match_lookup_job import ExactMatchLookupJob
				return ExactMatchLookupJob.model_validate(data)
			if mapping_key == "#microsoft.graph.exactMatchSessionBase":
				from .exact_match_session_base import ExactMatchSessionBase
				return ExactMatchSessionBase.model_validate(data)
			if mapping_key == "#microsoft.graph.exactMatchSession":
				from .exact_match_session import ExactMatchSession
				return ExactMatchSession.model_validate(data)
			if mapping_key == "#microsoft.graph.exactMatchUploadAgent":
				from .exact_match_upload_agent import ExactMatchUploadAgent
				return ExactMatchUploadAgent.model_validate(data)
			if mapping_key == "#microsoft.graph.exchangeAdmin":
				from .exchange_admin import ExchangeAdmin
				return ExchangeAdmin.model_validate(data)
			if mapping_key == "#microsoft.graph.exchangeSettings":
				from .exchange_settings import ExchangeSettings
				return ExchangeSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.extension":
				from .extension import Extension
				return Extension.model_validate(data)
			if mapping_key == "#microsoft.graph.openTypeExtension":
				from .open_type_extension import OpenTypeExtension
				return OpenTypeExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.personExtension":
				from .person_extension import PersonExtension
				return PersonExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.external":
				from .external import External
				return External.model_validate(data)
			if mapping_key == "#microsoft.graph.externalConnection":
				from .external_connection import ExternalConnection
				return ExternalConnection.model_validate(data)
			if mapping_key == "#microsoft.graph.externalDomainName":
				from .external_domain_name import ExternalDomainName
				return ExternalDomainName.model_validate(data)
			if mapping_key == "#microsoft.graph.externalGroup":
				from .external_group import ExternalGroup
				return ExternalGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.externalItem":
				from .external_item import ExternalItem
				return ExternalItem.model_validate(data)
			if mapping_key == "#microsoft.graph.featureRolloutPolicy":
				from .feature_rollout_policy import FeatureRolloutPolicy
				return FeatureRolloutPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.federatedIdentityCredential":
				from .federated_identity_credential import FederatedIdentityCredential
				return FederatedIdentityCredential.model_validate(data)
			if mapping_key == "#microsoft.graph.fieldValueSet":
				from .field_value_set import FieldValueSet
				return FieldValueSet.model_validate(data)
			if mapping_key == "#microsoft.graph.fileClassificationRequest":
				from .file_classification_request import FileClassificationRequest
				return FileClassificationRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.fileSecurityProfile":
				from .file_security_profile import FileSecurityProfile
				return FileSecurityProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.fileStorage":
				from .file_storage import FileStorage
				return FileStorage.model_validate(data)
			if mapping_key == "#microsoft.graph.fileStorageContainer":
				from .file_storage_container import FileStorageContainer
				return FileStorageContainer.model_validate(data)
			if mapping_key == "#microsoft.graph.filterOperatorSchema":
				from .filter_operator_schema import FilterOperatorSchema
				return FilterOperatorSchema.model_validate(data)
			if mapping_key == "#microsoft.graph.finding":
				from .finding import Finding
				return Finding.model_validate(data)
			if mapping_key == "#microsoft.graph.awsExternalSystemAccessFinding":
				from .aws_external_system_access_finding import AwsExternalSystemAccessFinding
				return AwsExternalSystemAccessFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.awsExternalSystemAccessRoleFinding":
				from .aws_external_system_access_role_finding import AwsExternalSystemAccessRoleFinding
				return AwsExternalSystemAccessRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.awsIdentityAccessManagementKeyAgeFinding":
				from .aws_identity_access_management_key_age_finding import AwsIdentityAccessManagementKeyAgeFinding
				return AwsIdentityAccessManagementKeyAgeFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.awsIdentityAccessManagementKeyUsageFinding":
				from .aws_identity_access_management_key_usage_finding import AwsIdentityAccessManagementKeyUsageFinding
				return AwsIdentityAccessManagementKeyUsageFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.awsSecretInformationAccessFinding":
				from .aws_secret_information_access_finding import AwsSecretInformationAccessFinding
				return AwsSecretInformationAccessFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.secretInformationAccessAwsResourceFinding":
				from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
				return SecretInformationAccessAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.secretInformationAccessAwsRoleFinding":
				from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
				return SecretInformationAccessAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.secretInformationAccessAwsServerlessFunctionFinding":
				from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
				return SecretInformationAccessAwsServerlessFunctionFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.secretInformationAccessAwsUserFinding":
				from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding
				return SecretInformationAccessAwsUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.awsSecurityToolAdministrationFinding":
				from .aws_security_tool_administration_finding import AwsSecurityToolAdministrationFinding
				return AwsSecurityToolAdministrationFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.securityToolAwsResourceAdministratorFinding":
				from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
				return SecurityToolAwsResourceAdministratorFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.securityToolAwsRoleAdministratorFinding":
				from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
				return SecurityToolAwsRoleAdministratorFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.securityToolAwsServerlessFunctionAdministratorFinding":
				from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
				return SecurityToolAwsServerlessFunctionAdministratorFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.securityToolAwsUserAdministratorFinding":
				from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding
				return SecurityToolAwsUserAdministratorFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.encryptedAwsStorageBucketFinding":
				from .encrypted_aws_storage_bucket_finding import EncryptedAwsStorageBucketFinding
				return EncryptedAwsStorageBucketFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.encryptedAzureStorageAccountFinding":
				from .encrypted_azure_storage_account_finding import EncryptedAzureStorageAccountFinding
				return EncryptedAzureStorageAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.encryptedGcpStorageBucketFinding":
				from .encrypted_gcp_storage_bucket_finding import EncryptedGcpStorageBucketFinding
				return EncryptedGcpStorageBucketFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.externallyAccessibleAwsStorageBucketFinding":
				from .externally_accessible_aws_storage_bucket_finding import ExternallyAccessibleAwsStorageBucketFinding
				return ExternallyAccessibleAwsStorageBucketFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.externallyAccessibleAzureBlobContainerFinding":
				from .externally_accessible_azure_blob_container_finding import ExternallyAccessibleAzureBlobContainerFinding
				return ExternallyAccessibleAzureBlobContainerFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.externallyAccessibleGcpStorageBucketFinding":
				from .externally_accessible_gcp_storage_bucket_finding import ExternallyAccessibleGcpStorageBucketFinding
				return ExternallyAccessibleGcpStorageBucketFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.identityFinding":
				from .identity_finding import IdentityFinding
				return IdentityFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveAwsResourceFinding":
				from .inactive_aws_resource_finding import InactiveAwsResourceFinding
				return InactiveAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveAwsRoleFinding":
				from .inactive_aws_role_finding import InactiveAwsRoleFinding
				return InactiveAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveAzureServicePrincipalFinding":
				from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
				return InactiveAzureServicePrincipalFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveGcpServiceAccountFinding":
				from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
				return InactiveGcpServiceAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveServerlessFunctionFinding":
				from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
				return InactiveServerlessFunctionFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveUserFinding":
				from .inactive_user_finding import InactiveUserFinding
				return InactiveUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedAwsResourceFinding":
				from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
				return OverprovisionedAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedAwsRoleFinding":
				from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
				return OverprovisionedAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedAzureServicePrincipalFinding":
				from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
				return OverprovisionedAzureServicePrincipalFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedGcpServiceAccountFinding":
				from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
				return OverprovisionedGcpServiceAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedServerlessFunctionFinding":
				from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
				return OverprovisionedServerlessFunctionFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedUserFinding":
				from .overprovisioned_user_finding import OverprovisionedUserFinding
				return OverprovisionedUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superAwsResourceFinding":
				from .super_aws_resource_finding import SuperAwsResourceFinding
				return SuperAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superAwsRoleFinding":
				from .super_aws_role_finding import SuperAwsRoleFinding
				return SuperAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superAzureServicePrincipalFinding":
				from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
				return SuperAzureServicePrincipalFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superGcpServiceAccountFinding":
				from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
				return SuperGcpServiceAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superServerlessFunctionFinding":
				from .super_serverless_function_finding import SuperServerlessFunctionFinding
				return SuperServerlessFunctionFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superUserFinding":
				from .super_user_finding import SuperUserFinding
				return SuperUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.unenforcedMfaAwsUserFinding":
				from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding
				return UnenforcedMfaAwsUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveGroupFinding":
				from .inactive_group_finding import InactiveGroupFinding
				return InactiveGroupFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.openAwsSecurityGroupFinding":
				from .open_aws_security_group_finding import OpenAwsSecurityGroupFinding
				return OpenAwsSecurityGroupFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.openNetworkAzureSecurityGroupFinding":
				from .open_network_azure_security_group_finding import OpenNetworkAzureSecurityGroupFinding
				return OpenNetworkAzureSecurityGroupFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalationFinding":
				from .privilege_escalation_finding import PrivilegeEscalationFinding
				return PrivilegeEscalationFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalationAwsResourceFinding":
				from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
				return PrivilegeEscalationAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalationAwsRoleFinding":
				from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
				return PrivilegeEscalationAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalationGcpServiceAccountFinding":
				from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
				return PrivilegeEscalationGcpServiceAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalationUserFinding":
				from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding
				return PrivilegeEscalationUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualMachineWithAwsStorageBucketAccessFinding":
				from .virtual_machine_with_aws_storage_bucket_access_finding import VirtualMachineWithAwsStorageBucketAccessFinding
				return VirtualMachineWithAwsStorageBucketAccessFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpRole":
				from .gcp_role import GcpRole
				return GcpRole.model_validate(data)
			if mapping_key == "#microsoft.graph.goals":
				from .goals import Goals
				return Goals.model_validate(data)
			if mapping_key == "#microsoft.graph.governanceInsight":
				from .governance_insight import GovernanceInsight
				return GovernanceInsight.model_validate(data)
			if mapping_key == "#microsoft.graph.membershipOutlierInsight":
				from .membership_outlier_insight import MembershipOutlierInsight
				return MembershipOutlierInsight.model_validate(data)
			if mapping_key == "#microsoft.graph.userSignInInsight":
				from .user_sign_in_insight import UserSignInInsight
				return UserSignInInsight.model_validate(data)
			if mapping_key == "#microsoft.graph.governancePolicyTemplate":
				from .governance_policy_template import GovernancePolicyTemplate
				return GovernancePolicyTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.governanceResource":
				from .governance_resource import GovernanceResource
				return GovernanceResource.model_validate(data)
			if mapping_key == "#microsoft.graph.governanceRoleAssignment":
				from .governance_role_assignment import GovernanceRoleAssignment
				return GovernanceRoleAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.governanceRoleAssignmentRequest":
				from .governance_role_assignment_request import GovernanceRoleAssignmentRequest
				return GovernanceRoleAssignmentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.governanceRoleDefinition":
				from .governance_role_definition import GovernanceRoleDefinition
				return GovernanceRoleDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.governanceRoleSetting":
				from .governance_role_setting import GovernanceRoleSetting
				return GovernanceRoleSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.governanceSubject":
				from .governance_subject import GovernanceSubject
				return GovernanceSubject.model_validate(data)
			if mapping_key == "#microsoft.graph.groupLifecyclePolicy":
				from .group_lifecycle_policy import GroupLifecyclePolicy
				return GroupLifecyclePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyCategory":
				from .group_policy_category import GroupPolicyCategory
				return GroupPolicyCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyConfiguration":
				from .group_policy_configuration import GroupPolicyConfiguration
				return GroupPolicyConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyConfigurationAssignment":
				from .group_policy_configuration_assignment import GroupPolicyConfigurationAssignment
				return GroupPolicyConfigurationAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyDefinition":
				from .group_policy_definition import GroupPolicyDefinition
				return GroupPolicyDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyDefinitionFile":
				from .group_policy_definition_file import GroupPolicyDefinitionFile
				return GroupPolicyDefinitionFile.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyUploadedDefinitionFile":
				from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile
				return GroupPolicyUploadedDefinitionFile.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyDefinitionValue":
				from .group_policy_definition_value import GroupPolicyDefinitionValue
				return GroupPolicyDefinitionValue.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyMigrationReport":
				from .group_policy_migration_report import GroupPolicyMigrationReport
				return GroupPolicyMigrationReport.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyObjectFile":
				from .group_policy_object_file import GroupPolicyObjectFile
				return GroupPolicyObjectFile.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyOperation":
				from .group_policy_operation import GroupPolicyOperation
				return GroupPolicyOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentation":
				from .group_policy_presentation import GroupPolicyPresentation
				return GroupPolicyPresentation.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyUploadedPresentation":
				from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation
				return GroupPolicyUploadedPresentation.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationCheckBox":
				from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
				return GroupPolicyPresentationCheckBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationComboBox":
				from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
				return GroupPolicyPresentationComboBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationDecimalTextBox":
				from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
				return GroupPolicyPresentationDecimalTextBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationDropdownList":
				from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
				return GroupPolicyPresentationDropdownList.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationListBox":
				from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
				return GroupPolicyPresentationListBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationLongDecimalTextBox":
				from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
				return GroupPolicyPresentationLongDecimalTextBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationMultiTextBox":
				from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
				return GroupPolicyPresentationMultiTextBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationText":
				from .group_policy_presentation_text import GroupPolicyPresentationText
				return GroupPolicyPresentationText.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationTextBox":
				from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox
				return GroupPolicyPresentationTextBox.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValue":
				from .group_policy_presentation_value import GroupPolicyPresentationValue
				return GroupPolicyPresentationValue.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValueBoolean":
				from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean
				return GroupPolicyPresentationValueBoolean.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValueDecimal":
				from .group_policy_presentation_value_decimal import GroupPolicyPresentationValueDecimal
				return GroupPolicyPresentationValueDecimal.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValueList":
				from .group_policy_presentation_value_list import GroupPolicyPresentationValueList
				return GroupPolicyPresentationValueList.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValueLongDecimal":
				from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal
				return GroupPolicyPresentationValueLongDecimal.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValueMultiText":
				from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText
				return GroupPolicyPresentationValueMultiText.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicyPresentationValueText":
				from .group_policy_presentation_value_text import GroupPolicyPresentationValueText
				return GroupPolicyPresentationValueText.model_validate(data)
			if mapping_key == "#microsoft.graph.groupPolicySettingMapping":
				from .group_policy_setting_mapping import GroupPolicySettingMapping
				return GroupPolicySettingMapping.model_validate(data)
			if mapping_key == "#microsoft.graph.hardwareConfiguration":
				from .hardware_configuration import HardwareConfiguration
				return HardwareConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.hardwareConfigurationAssignment":
				from .hardware_configuration_assignment import HardwareConfigurationAssignment
				return HardwareConfigurationAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.hardwareConfigurationDeviceState":
				from .hardware_configuration_device_state import HardwareConfigurationDeviceState
				return HardwareConfigurationDeviceState.model_validate(data)
			if mapping_key == "#microsoft.graph.hardwareConfigurationRunSummary":
				from .hardware_configuration_run_summary import HardwareConfigurationRunSummary
				return HardwareConfigurationRunSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.hardwareConfigurationUserState":
				from .hardware_configuration_user_state import HardwareConfigurationUserState
				return HardwareConfigurationUserState.model_validate(data)
			if mapping_key == "#microsoft.graph.hardwarePasswordDetail":
				from .hardware_password_detail import HardwarePasswordDetail
				return HardwarePasswordDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.hardwarePasswordInfo":
				from .hardware_password_info import HardwarePasswordInfo
				return HardwarePasswordInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.horizontalSection":
				from .horizontal_section import HorizontalSection
				return HorizontalSection.model_validate(data)
			if mapping_key == "#microsoft.graph.horizontalSectionColumn":
				from .horizontal_section_column import HorizontalSectionColumn
				return HorizontalSectionColumn.model_validate(data)
			if mapping_key == "#microsoft.graph.hostSecurityProfile":
				from .host_security_profile import HostSecurityProfile
				return HostSecurityProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.identityApiConnector":
				from .identity_api_connector import IdentityApiConnector
				return IdentityApiConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.identityProvider":
				from .identity_provider import IdentityProvider
				return IdentityProvider.model_validate(data)
			if mapping_key == "#microsoft.graph.openIdConnectProvider":
				from .open_id_connect_provider import OpenIdConnectProvider
				return OpenIdConnectProvider.model_validate(data)
			if mapping_key == "#microsoft.graph.identityProviderBase":
				from .identity_provider_base import IdentityProviderBase
				return IdentityProviderBase.model_validate(data)
			if mapping_key == "#microsoft.graph.appleManagedIdentityProvider":
				from .apple_managed_identity_provider import AppleManagedIdentityProvider
				return AppleManagedIdentityProvider.model_validate(data)
			if mapping_key == "#microsoft.graph.builtInIdentityProvider":
				from .built_in_identity_provider import BuiltInIdentityProvider
				return BuiltInIdentityProvider.model_validate(data)
			if mapping_key == "#microsoft.graph.oidcIdentityProvider":
				from .oidc_identity_provider import OidcIdentityProvider
				return OidcIdentityProvider.model_validate(data)
			if mapping_key == "#microsoft.graph.openIdConnectIdentityProvider":
				from .open_id_connect_identity_provider import OpenIdConnectIdentityProvider
				return OpenIdConnectIdentityProvider.model_validate(data)
			if mapping_key == "#microsoft.graph.samlOrWsFedProvider":
				from .saml_or_ws_fed_provider import SamlOrWsFedProvider
				return SamlOrWsFedProvider.model_validate(data)
			if mapping_key == "#microsoft.graph.internalDomainFederation":
				from .internal_domain_federation import InternalDomainFederation
				return InternalDomainFederation.model_validate(data)
			if mapping_key == "#microsoft.graph.samlOrWsFedExternalDomainFederation":
				from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
				return SamlOrWsFedExternalDomainFederation.model_validate(data)
			if mapping_key == "#microsoft.graph.socialIdentityProvider":
				from .social_identity_provider import SocialIdentityProvider
				return SocialIdentityProvider.model_validate(data)
			if mapping_key == "#microsoft.graph.identityUserFlow":
				from .identity_user_flow import IdentityUserFlow
				return IdentityUserFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.b2cIdentityUserFlow":
				from .b2c_identity_user_flow import B2cIdentityUserFlow
				return B2cIdentityUserFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.b2xIdentityUserFlow":
				from .b2x_identity_user_flow import B2xIdentityUserFlow
				return B2xIdentityUserFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.identityUserFlowAttribute":
				from .identity_user_flow_attribute import IdentityUserFlowAttribute
				return IdentityUserFlowAttribute.model_validate(data)
			if mapping_key == "#microsoft.graph.identityBuiltInUserFlowAttribute":
				from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
				return IdentityBuiltInUserFlowAttribute.model_validate(data)
			if mapping_key == "#microsoft.graph.identityCustomUserFlowAttribute":
				from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
				return IdentityCustomUserFlowAttribute.model_validate(data)
			if mapping_key == "#microsoft.graph.identityUserFlowAttributeAssignment":
				from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
				return IdentityUserFlowAttributeAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.impactedResource":
				from .impacted_resource import ImpactedResource
				return ImpactedResource.model_validate(data)
			if mapping_key == "#microsoft.graph.importedAppleDeviceIdentity":
				from .imported_apple_device_identity import ImportedAppleDeviceIdentity
				return ImportedAppleDeviceIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.importedAppleDeviceIdentityResult":
				from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult
				return ImportedAppleDeviceIdentityResult.model_validate(data)
			if mapping_key == "#microsoft.graph.importedDeviceIdentity":
				from .imported_device_identity import ImportedDeviceIdentity
				return ImportedDeviceIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.importedDeviceIdentityResult":
				from .imported_device_identity_result import ImportedDeviceIdentityResult
				return ImportedDeviceIdentityResult.model_validate(data)
			if mapping_key == "#microsoft.graph.importedWindowsAutopilotDeviceIdentity":
				from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
				return ImportedWindowsAutopilotDeviceIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.importedWindowsAutopilotDeviceIdentityUpload":
				from .imported_windows_autopilot_device_identity_upload import ImportedWindowsAutopilotDeviceIdentityUpload
				return ImportedWindowsAutopilotDeviceIdentityUpload.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveUsersByApplicationMetricBase":
				from .inactive_users_by_application_metric_base import InactiveUsersByApplicationMetricBase
				return InactiveUsersByApplicationMetricBase.model_validate(data)
			if mapping_key == "#microsoft.graph.dailyInactiveUsersByApplicationMetric":
				from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
				return DailyInactiveUsersByApplicationMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.monthlyInactiveUsersByApplicationMetric":
				from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric
				return MonthlyInactiveUsersByApplicationMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveUsersMetricBase":
				from .inactive_users_metric_base import InactiveUsersMetricBase
				return InactiveUsersMetricBase.model_validate(data)
			if mapping_key == "#microsoft.graph.dailyInactiveUsersMetric":
				from .daily_inactive_users_metric import DailyInactiveUsersMetric
				return DailyInactiveUsersMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.monthlyInactiveUsersMetric":
				from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric
				return MonthlyInactiveUsersMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.inferenceClassification":
				from .inference_classification import InferenceClassification
				return InferenceClassification.model_validate(data)
			if mapping_key == "#microsoft.graph.inferenceClassificationOverride":
				from .inference_classification_override import InferenceClassificationOverride
				return InferenceClassificationOverride.model_validate(data)
			if mapping_key == "#microsoft.graph.informationProtection":
				from .information_protection import InformationProtection
				return InformationProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.informationProtectionLabel":
				from .information_protection_label import InformationProtectionLabel
				return InformationProtectionLabel.model_validate(data)
			if mapping_key == "#microsoft.graph.informationProtectionPolicy":
				from .information_protection_policy import InformationProtectionPolicy
				return InformationProtectionPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.insightsSettings":
				from .insights_settings import InsightsSettings
				return InsightsSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.insightSummary":
				from .insight_summary import InsightSummary
				return InsightSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.internetExplorerMode":
				from .internet_explorer_mode import InternetExplorerMode
				return InternetExplorerMode.model_validate(data)
			if mapping_key == "#microsoft.graph.intuneBrandingProfile":
				from .intune_branding_profile import IntuneBrandingProfile
				return IntuneBrandingProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.intuneBrandingProfileAssignment":
				from .intune_branding_profile_assignment import IntuneBrandingProfileAssignment
				return IntuneBrandingProfileAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.invitation":
				from .invitation import Invitation
				return Invitation.model_validate(data)
			if mapping_key == "#microsoft.graph.iosLobAppProvisioningConfiguration":
				from .ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration
				return IosLobAppProvisioningConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosLobAppProvisioningConfigurationAssignment":
				from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
				return IosLobAppProvisioningConfigurationAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.iosUpdateDeviceStatus":
				from .ios_update_device_status import IosUpdateDeviceStatus
				return IosUpdateDeviceStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.iosVppAppAssignedLicense":
				from .ios_vpp_app_assigned_license import IosVppAppAssignedLicense
				return IosVppAppAssignedLicense.model_validate(data)
			if mapping_key == "#microsoft.graph.iosVppAppAssignedDeviceLicense":
				from .ios_vpp_app_assigned_device_license import IosVppAppAssignedDeviceLicense
				return IosVppAppAssignedDeviceLicense.model_validate(data)
			if mapping_key == "#microsoft.graph.iosVppAppAssignedUserLicense":
				from .ios_vpp_app_assigned_user_license import IosVppAppAssignedUserLicense
				return IosVppAppAssignedUserLicense.model_validate(data)
			if mapping_key == "#microsoft.graph.ipSecurityProfile":
				from .ip_security_profile import IpSecurityProfile
				return IpSecurityProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.itemActivity":
				from .item_activity import ItemActivity
				return ItemActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.itemActivityOLD":
				from .item_activity_o_l_d import ItemActivityOLD
				return ItemActivityOLD.model_validate(data)
			if mapping_key == "#microsoft.graph.itemActivityStat":
				from .item_activity_stat import ItemActivityStat
				return ItemActivityStat.model_validate(data)
			if mapping_key == "#microsoft.graph.itemAnalytics":
				from .item_analytics import ItemAnalytics
				return ItemAnalytics.model_validate(data)
			if mapping_key == "#microsoft.graph.itemFacet":
				from .item_facet import ItemFacet
				return ItemFacet.model_validate(data)
			if mapping_key == "#microsoft.graph.educationalActivity":
				from .educational_activity import EducationalActivity
				return EducationalActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.itemAddress":
				from .item_address import ItemAddress
				return ItemAddress.model_validate(data)
			if mapping_key == "#microsoft.graph.itemEmail":
				from .item_email import ItemEmail
				return ItemEmail.model_validate(data)
			if mapping_key == "#microsoft.graph.itemPatent":
				from .item_patent import ItemPatent
				return ItemPatent.model_validate(data)
			if mapping_key == "#microsoft.graph.itemPhone":
				from .item_phone import ItemPhone
				return ItemPhone.model_validate(data)
			if mapping_key == "#microsoft.graph.itemPublication":
				from .item_publication import ItemPublication
				return ItemPublication.model_validate(data)
			if mapping_key == "#microsoft.graph.languageProficiency":
				from .language_proficiency import LanguageProficiency
				return LanguageProficiency.model_validate(data)
			if mapping_key == "#microsoft.graph.personAnnotation":
				from .person_annotation import PersonAnnotation
				return PersonAnnotation.model_validate(data)
			if mapping_key == "#microsoft.graph.personAnnualEvent":
				from .person_annual_event import PersonAnnualEvent
				return PersonAnnualEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.personAward":
				from .person_award import PersonAward
				return PersonAward.model_validate(data)
			if mapping_key == "#microsoft.graph.personCertification":
				from .person_certification import PersonCertification
				return PersonCertification.model_validate(data)
			if mapping_key == "#microsoft.graph.personInterest":
				from .person_interest import PersonInterest
				return PersonInterest.model_validate(data)
			if mapping_key == "#microsoft.graph.personName":
				from .person_name import PersonName
				return PersonName.model_validate(data)
			if mapping_key == "#microsoft.graph.personResponsibility":
				from .person_responsibility import PersonResponsibility
				return PersonResponsibility.model_validate(data)
			if mapping_key == "#microsoft.graph.personWebsite":
				from .person_website import PersonWebsite
				return PersonWebsite.model_validate(data)
			if mapping_key == "#microsoft.graph.projectParticipation":
				from .project_participation import ProjectParticipation
				return ProjectParticipation.model_validate(data)
			if mapping_key == "#microsoft.graph.skillProficiency":
				from .skill_proficiency import SkillProficiency
				return SkillProficiency.model_validate(data)
			if mapping_key == "#microsoft.graph.userAccountInformation":
				from .user_account_information import UserAccountInformation
				return UserAccountInformation.model_validate(data)
			if mapping_key == "#microsoft.graph.webAccount":
				from .web_account import WebAccount
				return WebAccount.model_validate(data)
			if mapping_key == "#microsoft.graph.workPosition":
				from .work_position import WorkPosition
				return WorkPosition.model_validate(data)
			if mapping_key == "#microsoft.graph.itemRetentionLabel":
				from .item_retention_label import ItemRetentionLabel
				return ItemRetentionLabel.model_validate(data)
			if mapping_key == "#microsoft.graph.jobResponseBase":
				from .job_response_base import JobResponseBase
				return JobResponseBase.model_validate(data)
			if mapping_key == "#microsoft.graph.classificationJobResponse":
				from .classification_job_response import ClassificationJobResponse
				return ClassificationJobResponse.model_validate(data)
			if mapping_key == "#microsoft.graph.dlpEvaluatePoliciesJobResponse":
				from .dlp_evaluate_policies_job_response import DlpEvaluatePoliciesJobResponse
				return DlpEvaluatePoliciesJobResponse.model_validate(data)
			if mapping_key == "#microsoft.graph.evaluateLabelJobResponse":
				from .evaluate_label_job_response import EvaluateLabelJobResponse
				return EvaluateLabelJobResponse.model_validate(data)
			if mapping_key == "#microsoft.graph.landingPage":
				from .landing_page import LandingPage
				return LandingPage.model_validate(data)
			if mapping_key == "#microsoft.graph.landingPageDetail":
				from .landing_page_detail import LandingPageDetail
				return LandingPageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.learningContent":
				from .learning_content import LearningContent
				return LearningContent.model_validate(data)
			if mapping_key == "#microsoft.graph.learningCourseActivity":
				from .learning_course_activity import LearningCourseActivity
				return LearningCourseActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.learningAssignment":
				from .learning_assignment import LearningAssignment
				return LearningAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.learningSelfInitiatedCourse":
				from .learning_self_initiated_course import LearningSelfInitiatedCourse
				return LearningSelfInitiatedCourse.model_validate(data)
			if mapping_key == "#microsoft.graph.learningProvider":
				from .learning_provider import LearningProvider
				return LearningProvider.model_validate(data)
			if mapping_key == "#microsoft.graph.licenseDetails":
				from .license_details import LicenseDetails
				return LicenseDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.linkedResource":
				from .linked_resource import LinkedResource
				return LinkedResource.model_validate(data)
			if mapping_key == "#microsoft.graph.localizedNotificationMessage":
				from .localized_notification_message import LocalizedNotificationMessage
				return LocalizedNotificationMessage.model_validate(data)
			if mapping_key == "#microsoft.graph.loginPage":
				from .login_page import LoginPage
				return LoginPage.model_validate(data)
			if mapping_key == "#microsoft.graph.longRunningOperation":
				from .long_running_operation import LongRunningOperation
				return LongRunningOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.attackSimulationOperation":
				from .attack_simulation_operation import AttackSimulationOperation
				return AttackSimulationOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.engagementAsyncOperation":
				from .engagement_async_operation import EngagementAsyncOperation
				return EngagementAsyncOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.goalsExportJob":
				from .goals_export_job import GoalsExportJob
				return GoalsExportJob.model_validate(data)
			if mapping_key == "#microsoft.graph.richLongRunningOperation":
				from .rich_long_running_operation import RichLongRunningOperation
				return RichLongRunningOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.validateOperation":
				from .industry_data_validate_operation import IndustryDataValidateOperation
				return IndustryDataValidateOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.fileValidateOperation":
				from .industry_data_file_validate_operation import IndustryDataFileValidateOperation
				return IndustryDataFileValidateOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.lookupResultRow":
				from .lookup_result_row import LookupResultRow
				return LookupResultRow.model_validate(data)
			if mapping_key == "#microsoft.graph.m365AppsInstallationOptions":
				from .m365_apps_installation_options import M365AppsInstallationOptions
				return M365AppsInstallationOptions.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSSoftwareUpdateAccountSummary":
				from .mac_o_s_software_update_account_summary import MacOSSoftwareUpdateAccountSummary
				return MacOSSoftwareUpdateAccountSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSSoftwareUpdateCategorySummary":
				from .mac_o_s_software_update_category_summary import MacOSSoftwareUpdateCategorySummary
				return MacOSSoftwareUpdateCategorySummary.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSSoftwareUpdateStateSummary":
				from .mac_o_s_software_update_state_summary import MacOSSoftwareUpdateStateSummary
				return MacOSSoftwareUpdateStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.macOsVppAppAssignedLicense":
				from .mac_os_vpp_app_assigned_license import MacOsVppAppAssignedLicense
				return MacOsVppAppAssignedLicense.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxFolder":
				from .mailbox_folder import MailboxFolder
				return MailboxFolder.model_validate(data)
			if mapping_key == "#microsoft.graph.mailFolder":
				from .mail_folder import MailFolder
				return MailFolder.model_validate(data)
			if mapping_key == "#microsoft.graph.mailSearchFolder":
				from .mail_search_folder import MailSearchFolder
				return MailSearchFolder.model_validate(data)
			if mapping_key == "#microsoft.graph.mailFolderOperation":
				from .mail_folder_operation import MailFolderOperation
				return MailFolderOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.updateAllMessagesReadStateOperation":
				from .update_all_messages_read_state_operation import UpdateAllMessagesReadStateOperation
				return UpdateAllMessagesReadStateOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.malwareStateForWindowsDevice":
				from .malware_state_for_windows_device import MalwareStateForWindowsDevice
				return MalwareStateForWindowsDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAllDeviceCertificateState":
				from .managed_all_device_certificate_state import ManagedAllDeviceCertificateState
				return ManagedAllDeviceCertificateState.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppLogCollectionRequest":
				from .managed_app_log_collection_request import ManagedAppLogCollectionRequest
				return ManagedAppLogCollectionRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppOperation":
				from .managed_app_operation import ManagedAppOperation
				return ManagedAppOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppPolicy":
				from .managed_app_policy import ManagedAppPolicy
				return ManagedAppPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppConfiguration":
				from .managed_app_configuration import ManagedAppConfiguration
				return ManagedAppConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.targetedManagedAppConfiguration":
				from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
				return TargetedManagedAppConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppProtection":
				from .managed_app_protection import ManagedAppProtection
				return ManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.defaultManagedAppProtection":
				from .default_managed_app_protection import DefaultManagedAppProtection
				return DefaultManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.targetedManagedAppProtection":
				from .targeted_managed_app_protection import TargetedManagedAppProtection
				return TargetedManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.androidManagedAppProtection":
				from .android_managed_app_protection import AndroidManagedAppProtection
				return AndroidManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.iosManagedAppProtection":
				from .ios_managed_app_protection import IosManagedAppProtection
				return IosManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtection":
				from .windows_information_protection import WindowsInformationProtection
				return WindowsInformationProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.mdmWindowsInformationProtectionPolicy":
				from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
				return MdmWindowsInformationProtectionPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtectionPolicy":
				from .windows_information_protection_policy import WindowsInformationProtectionPolicy
				return WindowsInformationProtectionPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsManagedAppProtection":
				from .windows_managed_app_protection import WindowsManagedAppProtection
				return WindowsManagedAppProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppPolicyDeploymentSummary":
				from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
				return ManagedAppPolicyDeploymentSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppRegistration":
				from .managed_app_registration import ManagedAppRegistration
				return ManagedAppRegistration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidManagedAppRegistration":
				from .android_managed_app_registration import AndroidManagedAppRegistration
				return AndroidManagedAppRegistration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosManagedAppRegistration":
				from .ios_managed_app_registration import IosManagedAppRegistration
				return IosManagedAppRegistration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsManagedAppRegistration":
				from .windows_managed_app_registration import WindowsManagedAppRegistration
				return WindowsManagedAppRegistration.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppStatus":
				from .managed_app_status import ManagedAppStatus
				return ManagedAppStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppStatusRaw":
				from .managed_app_status_raw import ManagedAppStatusRaw
				return ManagedAppStatusRaw.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDevice":
				from .managed_device import ManagedDevice
				return ManagedDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsManagedDevice":
				from .windows_managed_device import WindowsManagedDevice
				return WindowsManagedDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceCertificateState":
				from .managed_device_certificate_state import ManagedDeviceCertificateState
				return ManagedDeviceCertificateState.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceCleanupRule":
				from .managed_device_cleanup_rule import ManagedDeviceCleanupRule
				return ManagedDeviceCleanupRule.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceEncryptionState":
				from .managed_device_encryption_state import ManagedDeviceEncryptionState
				return ManagedDeviceEncryptionState.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceMobileAppConfiguration":
				from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
				return ManagedDeviceMobileAppConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkMobileAppConfiguration":
				from .android_for_work_mobile_app_configuration import AndroidForWorkMobileAppConfiguration
				return AndroidForWorkMobileAppConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidManagedStoreAppConfiguration":
				from .android_managed_store_app_configuration import AndroidManagedStoreAppConfiguration
				return AndroidManagedStoreAppConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosMobileAppConfiguration":
				from .ios_mobile_app_configuration import IosMobileAppConfiguration
				return IosMobileAppConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceMobileAppConfigurationAssignment":
				from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
				return ManagedDeviceMobileAppConfigurationAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceMobileAppConfigurationDeviceStatus":
				from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
				return ManagedDeviceMobileAppConfigurationDeviceStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceMobileAppConfigurationDeviceSummary":
				from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
				return ManagedDeviceMobileAppConfigurationDeviceSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceMobileAppConfigurationState":
				from .managed_device_mobile_app_configuration_state import ManagedDeviceMobileAppConfigurationState
				return ManagedDeviceMobileAppConfigurationState.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceMobileAppConfigurationUserStatus":
				from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
				return ManagedDeviceMobileAppConfigurationUserStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceMobileAppConfigurationUserSummary":
				from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary
				return ManagedDeviceMobileAppConfigurationUserSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceOverview":
				from .managed_device_overview import ManagedDeviceOverview
				return ManagedDeviceOverview.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceWindowsOperatingSystemImage":
				from .managed_device_windows_operating_system_image import ManagedDeviceWindowsOperatingSystemImage
				return ManagedDeviceWindowsOperatingSystemImage.model_validate(data)
			if mapping_key == "#microsoft.graph.managedEBook":
				from .managed_e_book import ManagedEBook
				return ManagedEBook.model_validate(data)
			if mapping_key == "#microsoft.graph.iosVppEBook":
				from .ios_vpp_e_book import IosVppEBook
				return IosVppEBook.model_validate(data)
			if mapping_key == "#microsoft.graph.managedEBookAssignment":
				from .managed_e_book_assignment import ManagedEBookAssignment
				return ManagedEBookAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.iosVppEBookAssignment":
				from .ios_vpp_e_book_assignment import IosVppEBookAssignment
				return IosVppEBookAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.managedEBookCategory":
				from .managed_e_book_category import ManagedEBookCategory
				return ManagedEBookCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.managedMobileApp":
				from .managed_mobile_app import ManagedMobileApp
				return ManagedMobileApp.model_validate(data)
			if mapping_key == "#microsoft.graph.meetingAttendanceReport":
				from .meeting_attendance_report import MeetingAttendanceReport
				return MeetingAttendanceReport.model_validate(data)
			if mapping_key == "#microsoft.graph.meetingRegistrantBase":
				from .meeting_registrant_base import MeetingRegistrantBase
				return MeetingRegistrantBase.model_validate(data)
			if mapping_key == "#microsoft.graph.externalMeetingRegistrant":
				from .external_meeting_registrant import ExternalMeetingRegistrant
				return ExternalMeetingRegistrant.model_validate(data)
			if mapping_key == "#microsoft.graph.meetingRegistrant":
				from .meeting_registrant import MeetingRegistrant
				return MeetingRegistrant.model_validate(data)
			if mapping_key == "#microsoft.graph.meetingRegistrationBase":
				from .meeting_registration_base import MeetingRegistrationBase
				return MeetingRegistrationBase.model_validate(data)
			if mapping_key == "#microsoft.graph.externalMeetingRegistration":
				from .external_meeting_registration import ExternalMeetingRegistration
				return ExternalMeetingRegistration.model_validate(data)
			if mapping_key == "#microsoft.graph.meetingRegistration":
				from .meeting_registration import MeetingRegistration
				return MeetingRegistration.model_validate(data)
			if mapping_key == "#microsoft.graph.meetingRegistrationQuestion":
				from .meeting_registration_question import MeetingRegistrationQuestion
				return MeetingRegistrationQuestion.model_validate(data)
			if mapping_key == "#microsoft.graph.mention":
				from .mention import Mention
				return Mention.model_validate(data)
			if mapping_key == "#microsoft.graph.messageEvent":
				from .message_event import MessageEvent
				return MessageEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.messageRecipient":
				from .message_recipient import MessageRecipient
				return MessageRecipient.model_validate(data)
			if mapping_key == "#microsoft.graph.messageRule":
				from .message_rule import MessageRule
				return MessageRule.model_validate(data)
			if mapping_key == "#microsoft.graph.messageTrace":
				from .message_trace import MessageTrace
				return MessageTrace.model_validate(data)
			if mapping_key == "#microsoft.graph.mfaCompletionMetric":
				from .mfa_completion_metric import MfaCompletionMetric
				return MfaCompletionMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.mfaFailure":
				from .mfa_failure import MfaFailure
				return MfaFailure.model_validate(data)
			if mapping_key == "#microsoft.graph.mfaTelecomFraudMetric":
				from .mfa_telecom_fraud_metric import MfaTelecomFraudMetric
				return MfaTelecomFraudMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.mfaUserCountMetric":
				from .mfa_user_count_metric import MfaUserCountMetric
				return MfaUserCountMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftApplicationDataAccessSettings":
				from .microsoft_application_data_access_settings import MicrosoftApplicationDataAccessSettings
				return MicrosoftApplicationDataAccessSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftTunnelConfiguration":
				from .microsoft_tunnel_configuration import MicrosoftTunnelConfiguration
				return MicrosoftTunnelConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftTunnelHealthThreshold":
				from .microsoft_tunnel_health_threshold import MicrosoftTunnelHealthThreshold
				return MicrosoftTunnelHealthThreshold.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftTunnelServer":
				from .microsoft_tunnel_server import MicrosoftTunnelServer
				return MicrosoftTunnelServer.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftTunnelServerLogCollectionResponse":
				from .microsoft_tunnel_server_log_collection_response import MicrosoftTunnelServerLogCollectionResponse
				return MicrosoftTunnelServerLogCollectionResponse.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftTunnelSite":
				from .microsoft_tunnel_site import MicrosoftTunnelSite
				return MicrosoftTunnelSite.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileApp":
				from .mobile_app import MobileApp
				return MobileApp.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkApp":
				from .android_for_work_app import AndroidForWorkApp
				return AndroidForWorkApp.model_validate(data)
			if mapping_key == "#microsoft.graph.androidManagedStoreApp":
				from .android_managed_store_app import AndroidManagedStoreApp
				return AndroidManagedStoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.androidManagedStoreWebApp":
				from .android_managed_store_web_app import AndroidManagedStoreWebApp
				return AndroidManagedStoreWebApp.model_validate(data)
			if mapping_key == "#microsoft.graph.androidStoreApp":
				from .android_store_app import AndroidStoreApp
				return AndroidStoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.iosiPadOSWebClip":
				from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
				return IosiPadOSWebClip.model_validate(data)
			if mapping_key == "#microsoft.graph.iosStoreApp":
				from .ios_store_app import IosStoreApp
				return IosStoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.iosVppApp":
				from .ios_vpp_app import IosVppApp
				return IosVppApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSMicrosoftDefenderApp":
				from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
				return MacOSMicrosoftDefenderApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSMicrosoftEdgeApp":
				from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
				return MacOSMicrosoftEdgeApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSOfficeSuiteApp":
				from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
				return MacOSOfficeSuiteApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOsVppApp":
				from .mac_os_vpp_app import MacOsVppApp
				return MacOsVppApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSWebClip":
				from .mac_o_s_web_clip import MacOSWebClip
				return MacOSWebClip.model_validate(data)
			if mapping_key == "#microsoft.graph.managedApp":
				from .managed_app import ManagedApp
				return ManagedApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAndroidStoreApp":
				from .managed_android_store_app import ManagedAndroidStoreApp
				return ManagedAndroidStoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedIOSStoreApp":
				from .managed_i_o_s_store_app import ManagedIOSStoreApp
				return ManagedIOSStoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedMobileLobApp":
				from .managed_mobile_lob_app import ManagedMobileLobApp
				return ManagedMobileLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAndroidLobApp":
				from .managed_android_lob_app import ManagedAndroidLobApp
				return ManagedAndroidLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.managedIOSLobApp":
				from .managed_i_o_s_lob_app import ManagedIOSLobApp
				return ManagedIOSLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftStoreForBusinessApp":
				from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
				return MicrosoftStoreForBusinessApp.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileLobApp":
				from .mobile_lob_app import MobileLobApp
				return MobileLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.androidLobApp":
				from .android_lob_app import AndroidLobApp
				return AndroidLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.iosLobApp":
				from .ios_lob_app import IosLobApp
				return IosLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSDmgApp":
				from .mac_o_s_dmg_app import MacOSDmgApp
				return MacOSDmgApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSLobApp":
				from .mac_o_s_lob_app import MacOSLobApp
				return MacOSLobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSPkgApp":
				from .mac_o_s_pkg_app import MacOSPkgApp
				return MacOSPkgApp.model_validate(data)
			if mapping_key == "#microsoft.graph.win32LobApp":
				from .win32_lob_app import Win32LobApp
				return Win32LobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.win32CatalogApp":
				from .win32_catalog_app import Win32CatalogApp
				return Win32CatalogApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAppX":
				from .windows_app_x import WindowsAppX
				return WindowsAppX.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsMobileMSI":
				from .windows_mobile_m_s_i import WindowsMobileMSI
				return WindowsMobileMSI.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81AppX":
				from .windows_phone81_app_x import WindowsPhone81AppX
				return WindowsPhone81AppX.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81AppXBundle":
				from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle
				return WindowsPhone81AppXBundle.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhoneXAP":
				from .windows_phone_x_a_p import WindowsPhoneXAP
				return WindowsPhoneXAP.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUniversalAppX":
				from .windows_universal_app_x import WindowsUniversalAppX
				return WindowsUniversalAppX.model_validate(data)
			if mapping_key == "#microsoft.graph.officeSuiteApp":
				from .office_suite_app import OfficeSuiteApp
				return OfficeSuiteApp.model_validate(data)
			if mapping_key == "#microsoft.graph.webApp":
				from .web_app import WebApp
				return WebApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsMicrosoftEdgeApp":
				from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
				return WindowsMicrosoftEdgeApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81StoreApp":
				from .windows_phone81_store_app import WindowsPhone81StoreApp
				return WindowsPhone81StoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsStoreApp":
				from .windows_store_app import WindowsStoreApp
				return WindowsStoreApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsWebApp":
				from .windows_web_app import WindowsWebApp
				return WindowsWebApp.model_validate(data)
			if mapping_key == "#microsoft.graph.winGetApp":
				from .win_get_app import WinGetApp
				return WinGetApp.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppAssignment":
				from .mobile_app_assignment import MobileAppAssignment
				return MobileAppAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppCatalogPackage":
				from .mobile_app_catalog_package import MobileAppCatalogPackage
				return MobileAppCatalogPackage.model_validate(data)
			if mapping_key == "#microsoft.graph.win32MobileAppCatalogPackage":
				from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage
				return Win32MobileAppCatalogPackage.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppCategory":
				from .mobile_app_category import MobileAppCategory
				return MobileAppCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppContent":
				from .mobile_app_content import MobileAppContent
				return MobileAppContent.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppContentFile":
				from .mobile_app_content_file import MobileAppContentFile
				return MobileAppContentFile.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppInstallStatus":
				from .mobile_app_install_status import MobileAppInstallStatus
				return MobileAppInstallStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppInstallSummary":
				from .mobile_app_install_summary import MobileAppInstallSummary
				return MobileAppInstallSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppIntentAndState":
				from .mobile_app_intent_and_state import MobileAppIntentAndState
				return MobileAppIntentAndState.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppProvisioningConfigGroupAssignment":
				from .mobile_app_provisioning_config_group_assignment import MobileAppProvisioningConfigGroupAssignment
				return MobileAppProvisioningConfigGroupAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppRelationship":
				from .mobile_app_relationship import MobileAppRelationship
				return MobileAppRelationship.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppDependency":
				from .mobile_app_dependency import MobileAppDependency
				return MobileAppDependency.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppSupersedence":
				from .mobile_app_supersedence import MobileAppSupersedence
				return MobileAppSupersedence.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileContainedApp":
				from .mobile_contained_app import MobileContainedApp
				return MobileContainedApp.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftStoreForBusinessContainedApp":
				from .microsoft_store_for_business_contained_app import MicrosoftStoreForBusinessContainedApp
				return MicrosoftStoreForBusinessContainedApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUniversalAppXContainedApp":
				from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp
				return WindowsUniversalAppXContainedApp.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileThreatDefenseConnector":
				from .mobile_threat_defense_connector import MobileThreatDefenseConnector
				return MobileThreatDefenseConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.mobilityManagementPolicy":
				from .mobility_management_policy import MobilityManagementPolicy
				return MobilityManagementPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.monthlyUserInsightMetricsRoot":
				from .monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot
				return MonthlyUserInsightMetricsRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.multiTenantOrganization":
				from .multi_tenant_organization import MultiTenantOrganization
				return MultiTenantOrganization.model_validate(data)
			if mapping_key == "#microsoft.graph.multiTenantOrganizationIdentitySyncPolicyTemplate":
				from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate
				return MultiTenantOrganizationIdentitySyncPolicyTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.multiTenantOrganizationJoinRequestRecord":
				from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
				return MultiTenantOrganizationJoinRequestRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.multiTenantOrganizationPartnerConfigurationTemplate":
				from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate
				return MultiTenantOrganizationPartnerConfigurationTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.multiValueLegacyExtendedProperty":
				from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
				return MultiValueLegacyExtendedProperty.model_validate(data)
			if mapping_key == "#microsoft.graph.namedLocation":
				from .named_location import NamedLocation
				return NamedLocation.model_validate(data)
			if mapping_key == "#microsoft.graph.compliantNetworkNamedLocation":
				from .compliant_network_named_location import CompliantNetworkNamedLocation
				return CompliantNetworkNamedLocation.model_validate(data)
			if mapping_key == "#microsoft.graph.countryNamedLocation":
				from .country_named_location import CountryNamedLocation
				return CountryNamedLocation.model_validate(data)
			if mapping_key == "#microsoft.graph.ipNamedLocation":
				from .ip_named_location import IpNamedLocation
				return IpNamedLocation.model_validate(data)
			if mapping_key == "#microsoft.graph.namePronunciationSettings":
				from .name_pronunciation_settings import NamePronunciationSettings
				return NamePronunciationSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.ndesConnector":
				from .ndes_connector import NdesConnector
				return NdesConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.notification":
				from .notification import Notification
				return Notification.model_validate(data)
			if mapping_key == "#microsoft.graph.notificationMessageTemplate":
				from .notification_message_template import NotificationMessageTemplate
				return NotificationMessageTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.oAuth2PermissionGrant":
				from .o_auth2_permission_grant import OAuth2PermissionGrant
				return OAuth2PermissionGrant.model_validate(data)
			if mapping_key == "#microsoft.graph.office365ActiveUserCounts":
				from .office365_active_user_counts import Office365ActiveUserCounts
				return Office365ActiveUserCounts.model_validate(data)
			if mapping_key == "#microsoft.graph.office365ActiveUserDetail":
				from .office365_active_user_detail import Office365ActiveUserDetail
				return Office365ActiveUserDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.office365GroupsActivityCounts":
				from .office365_groups_activity_counts import Office365GroupsActivityCounts
				return Office365GroupsActivityCounts.model_validate(data)
			if mapping_key == "#microsoft.graph.office365GroupsActivityDetail":
				from .office365_groups_activity_detail import Office365GroupsActivityDetail
				return Office365GroupsActivityDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.office365GroupsActivityFileCounts":
				from .office365_groups_activity_file_counts import Office365GroupsActivityFileCounts
				return Office365GroupsActivityFileCounts.model_validate(data)
			if mapping_key == "#microsoft.graph.office365GroupsActivityGroupCounts":
				from .office365_groups_activity_group_counts import Office365GroupsActivityGroupCounts
				return Office365GroupsActivityGroupCounts.model_validate(data)
			if mapping_key == "#microsoft.graph.office365GroupsActivityStorage":
				from .office365_groups_activity_storage import Office365GroupsActivityStorage
				return Office365GroupsActivityStorage.model_validate(data)
			if mapping_key == "#microsoft.graph.office365ServicesUserCounts":
				from .office365_services_user_counts import Office365ServicesUserCounts
				return Office365ServicesUserCounts.model_validate(data)
			if mapping_key == "#microsoft.graph.officeGraphInsights":
				from .office_graph_insights import OfficeGraphInsights
				return OfficeGraphInsights.model_validate(data)
			if mapping_key == "#microsoft.graph.itemInsights":
				from .item_insights import ItemInsights
				return ItemInsights.model_validate(data)
			if mapping_key == "#microsoft.graph.onenote":
				from .onenote import Onenote
				return Onenote.model_validate(data)
			if mapping_key == "#microsoft.graph.onenoteEntityBaseModel":
				from .onenote_entity_base_model import OnenoteEntityBaseModel
				return OnenoteEntityBaseModel.model_validate(data)
			if mapping_key == "#microsoft.graph.onenoteEntitySchemaObjectModel":
				from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
				return OnenoteEntitySchemaObjectModel.model_validate(data)
			if mapping_key == "#microsoft.graph.onenoteEntityHierarchyModel":
				from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
				return OnenoteEntityHierarchyModel.model_validate(data)
			if mapping_key == "#microsoft.graph.notebook":
				from .notebook import Notebook
				return Notebook.model_validate(data)
			if mapping_key == "#microsoft.graph.onenoteSection":
				from .onenote_section import OnenoteSection
				return OnenoteSection.model_validate(data)
			if mapping_key == "#microsoft.graph.sectionGroup":
				from .section_group import SectionGroup
				return SectionGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.onenotePage":
				from .onenote_page import OnenotePage
				return OnenotePage.model_validate(data)
			if mapping_key == "#microsoft.graph.onenoteResource":
				from .onenote_resource import OnenoteResource
				return OnenoteResource.model_validate(data)
			if mapping_key == "#microsoft.graph.onlineMeetingBase":
				from .online_meeting_base import OnlineMeetingBase
				return OnlineMeetingBase.model_validate(data)
			if mapping_key == "#microsoft.graph.onlineMeeting":
				from .online_meeting import OnlineMeeting
				return OnlineMeeting.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventSession":
				from .virtual_event_session import VirtualEventSession
				return VirtualEventSession.model_validate(data)
			if mapping_key == "#microsoft.graph.onPremisesAgent":
				from .on_premises_agent import OnPremisesAgent
				return OnPremisesAgent.model_validate(data)
			if mapping_key == "#microsoft.graph.onPremisesAgentGroup":
				from .on_premises_agent_group import OnPremisesAgentGroup
				return OnPremisesAgentGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.onPremisesConditionalAccessSettings":
				from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
				return OnPremisesConditionalAccessSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.onPremisesDirectorySynchronization":
				from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
				return OnPremisesDirectorySynchronization.model_validate(data)
			if mapping_key == "#microsoft.graph.onPremisesPublishingProfile":
				from .on_premises_publishing_profile import OnPremisesPublishingProfile
				return OnPremisesPublishingProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.operation":
				from .operation import Operation
				return Operation.model_validate(data)
			if mapping_key == "#microsoft.graph.onenoteOperation":
				from .onenote_operation import OnenoteOperation
				return OnenoteOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.operationApprovalPolicy":
				from .operation_approval_policy import OperationApprovalPolicy
				return OperationApprovalPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.operationApprovalRequest":
				from .operation_approval_request import OperationApprovalRequest
				return OperationApprovalRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.organizationalBrandingProperties":
				from .organizational_branding_properties import OrganizationalBrandingProperties
				return OrganizationalBrandingProperties.model_validate(data)
			if mapping_key == "#microsoft.graph.organizationalBranding":
				from .organizational_branding import OrganizationalBranding
				return OrganizationalBranding.model_validate(data)
			if mapping_key == "#microsoft.graph.organizationalBrandingLocalization":
				from .organizational_branding_localization import OrganizationalBrandingLocalization
				return OrganizationalBrandingLocalization.model_validate(data)
			if mapping_key == "#microsoft.graph.organizationSettings":
				from .organization_settings import OrganizationSettings
				return OrganizationSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.outlookCategory":
				from .outlook_category import OutlookCategory
				return OutlookCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.outlookItem":
				from .outlook_item import OutlookItem
				return OutlookItem.model_validate(data)
			if mapping_key == "#microsoft.graph.contact":
				from .contact import Contact
				return Contact.model_validate(data)
			if mapping_key == "#microsoft.graph.event":
				from .event import Event
				return Event.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxItem":
				from .mailbox_item import MailboxItem
				return MailboxItem.model_validate(data)
			if mapping_key == "#microsoft.graph.message":
				from .message import Message
				return Message.model_validate(data)
			if mapping_key == "#microsoft.graph.calendarSharingMessage":
				from .calendar_sharing_message import CalendarSharingMessage
				return CalendarSharingMessage.model_validate(data)
			if mapping_key == "#microsoft.graph.eventMessage":
				from .event_message import EventMessage
				return EventMessage.model_validate(data)
			if mapping_key == "#microsoft.graph.eventMessageRequest":
				from .event_message_request import EventMessageRequest
				return EventMessageRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.eventMessageResponse":
				from .event_message_response import EventMessageResponse
				return EventMessageResponse.model_validate(data)
			if mapping_key == "#microsoft.graph.note":
				from .note import Note
				return Note.model_validate(data)
			if mapping_key == "#microsoft.graph.outlookTask":
				from .outlook_task import OutlookTask
				return OutlookTask.model_validate(data)
			if mapping_key == "#microsoft.graph.post":
				from .post import Post
				return Post.model_validate(data)
			if mapping_key == "#microsoft.graph.outlookTaskFolder":
				from .outlook_task_folder import OutlookTaskFolder
				return OutlookTaskFolder.model_validate(data)
			if mapping_key == "#microsoft.graph.outlookTaskGroup":
				from .outlook_task_group import OutlookTaskGroup
				return OutlookTaskGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.outlookUser":
				from .outlook_user import OutlookUser
				return OutlookUser.model_validate(data)
			if mapping_key == "#microsoft.graph.participant":
				from .participant import Participant
				return Participant.model_validate(data)
			if mapping_key == "#microsoft.graph.participantJoiningNotification":
				from .participant_joining_notification import ParticipantJoiningNotification
				return ParticipantJoiningNotification.model_validate(data)
			if mapping_key == "#microsoft.graph.participantLeftNotification":
				from .participant_left_notification import ParticipantLeftNotification
				return ParticipantLeftNotification.model_validate(data)
			if mapping_key == "#microsoft.graph.partners":
				from .partners import Partners
				return Partners.model_validate(data)
			if mapping_key == "#microsoft.graph.payload":
				from .payload import Payload
				return Payload.model_validate(data)
			if mapping_key == "#microsoft.graph.payloadResponse":
				from .payload_response import PayloadResponse
				return PayloadResponse.model_validate(data)
			if mapping_key == "#microsoft.graph.peopleAdminSettings":
				from .people_admin_settings import PeopleAdminSettings
				return PeopleAdminSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.permission":
				from .permission import Permission
				return Permission.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionGrantConditionSet":
				from .permission_grant_condition_set import PermissionGrantConditionSet
				return PermissionGrantConditionSet.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionsAnalytics":
				from .permissions_analytics import PermissionsAnalytics
				return PermissionsAnalytics.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionsAnalyticsAggregation":
				from .permissions_analytics_aggregation import PermissionsAnalyticsAggregation
				return PermissionsAnalyticsAggregation.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionsCreepIndexDistribution":
				from .permissions_creep_index_distribution import PermissionsCreepIndexDistribution
				return PermissionsCreepIndexDistribution.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionsDefinitionAwsPolicy":
				from .permissions_definition_aws_policy import PermissionsDefinitionAwsPolicy
				return PermissionsDefinitionAwsPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionsDefinitionAzureRole":
				from .permissions_definition_azure_role import PermissionsDefinitionAzureRole
				return PermissionsDefinitionAzureRole.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionsDefinitionGcpRole":
				from .permissions_definition_gcp_role import PermissionsDefinitionGcpRole
				return PermissionsDefinitionGcpRole.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionsManagement":
				from .permissions_management import PermissionsManagement
				return PermissionsManagement.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionsRequestChange":
				from .permissions_request_change import PermissionsRequestChange
				return PermissionsRequestChange.model_validate(data)
			if mapping_key == "#microsoft.graph.person":
				from .person import Person
				return Person.model_validate(data)
			if mapping_key == "#microsoft.graph.pinnedChatMessageInfo":
				from .pinned_chat_message_info import PinnedChatMessageInfo
				return PinnedChatMessageInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.place":
				from .place import Place
				return Place.model_validate(data)
			if mapping_key == "#microsoft.graph.room":
				from .room import Room
				return Room.model_validate(data)
			if mapping_key == "#microsoft.graph.roomList":
				from .room_list import RoomList
				return RoomList.model_validate(data)
			if mapping_key == "#microsoft.graph.workspace":
				from .workspace import Workspace
				return Workspace.model_validate(data)
			if mapping_key == "#microsoft.graph.planner":
				from .planner import Planner
				return Planner.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerDelta":
				from .planner_delta import PlannerDelta
				return PlannerDelta.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerAssignedToTaskBoardTaskFormat":
				from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
				return PlannerAssignedToTaskBoardTaskFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerBucket":
				from .planner_bucket import PlannerBucket
				return PlannerBucket.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerBucketTaskBoardTaskFormat":
				from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
				return PlannerBucketTaskBoardTaskFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerPlan":
				from .planner_plan import PlannerPlan
				return PlannerPlan.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerPlanDetails":
				from .planner_plan_details import PlannerPlanDetails
				return PlannerPlanDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerProgressTaskBoardTaskFormat":
				from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
				return PlannerProgressTaskBoardTaskFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerTask":
				from .planner_task import PlannerTask
				return PlannerTask.model_validate(data)
			if mapping_key == "#microsoft.graph.businessScenarioTask":
				from .business_scenario_task import BusinessScenarioTask
				return BusinessScenarioTask.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerTaskDetails":
				from .planner_task_details import PlannerTaskDetails
				return PlannerTaskDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerUser":
				from .planner_user import PlannerUser
				return PlannerUser.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerGroup":
				from .planner_group import PlannerGroup
				return PlannerGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerPlanConfiguration":
				from .planner_plan_configuration import PlannerPlanConfiguration
				return PlannerPlanConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerPlanConfigurationLocalization":
				from .planner_plan_configuration_localization import PlannerPlanConfigurationLocalization
				return PlannerPlanConfigurationLocalization.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerRoster":
				from .planner_roster import PlannerRoster
				return PlannerRoster.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerRosterMember":
				from .planner_roster_member import PlannerRosterMember
				return PlannerRosterMember.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerTaskConfiguration":
				from .planner_task_configuration import PlannerTaskConfiguration
				return PlannerTaskConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.policyRoot":
				from .policy_root import PolicyRoot
				return PolicyRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.policySet":
				from .policy_set import PolicySet
				return PolicySet.model_validate(data)
			if mapping_key == "#microsoft.graph.policySetAssignment":
				from .policy_set_assignment import PolicySetAssignment
				return PolicySetAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.policySetItem":
				from .policy_set_item import PolicySetItem
				return PolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceCompliancePolicyPolicySetItem":
				from .device_compliance_policy_policy_set_item import DeviceCompliancePolicyPolicySetItem
				return DeviceCompliancePolicyPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationPolicySetItem":
				from .device_configuration_policy_set_item import DeviceConfigurationPolicySetItem
				return DeviceConfigurationPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationPolicyPolicySetItem":
				from .device_management_configuration_policy_policy_set_item import DeviceManagementConfigurationPolicyPolicySetItem
				return DeviceManagementConfigurationPolicyPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementScriptPolicySetItem":
				from .device_management_script_policy_set_item import DeviceManagementScriptPolicySetItem
				return DeviceManagementScriptPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.enrollmentRestrictionsConfigurationPolicySetItem":
				from .enrollment_restrictions_configuration_policy_set_item import EnrollmentRestrictionsConfigurationPolicySetItem
				return EnrollmentRestrictionsConfigurationPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.iosLobAppProvisioningConfigurationPolicySetItem":
				from .ios_lob_app_provisioning_configuration_policy_set_item import IosLobAppProvisioningConfigurationPolicySetItem
				return IosLobAppProvisioningConfigurationPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppProtectionPolicySetItem":
				from .managed_app_protection_policy_set_item import ManagedAppProtectionPolicySetItem
				return ManagedAppProtectionPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceMobileAppConfigurationPolicySetItem":
				from .managed_device_mobile_app_configuration_policy_set_item import ManagedDeviceMobileAppConfigurationPolicySetItem
				return ManagedDeviceMobileAppConfigurationPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.mdmWindowsInformationProtectionPolicyPolicySetItem":
				from .mdm_windows_information_protection_policy_policy_set_item import MdmWindowsInformationProtectionPolicyPolicySetItem
				return MdmWindowsInformationProtectionPolicyPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppPolicySetItem":
				from .mobile_app_policy_set_item import MobileAppPolicySetItem
				return MobileAppPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.targetedManagedAppConfigurationPolicySetItem":
				from .targeted_managed_app_configuration_policy_set_item import TargetedManagedAppConfigurationPolicySetItem
				return TargetedManagedAppConfigurationPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EnrollmentCompletionPageConfigurationPolicySetItem":
				from .windows10_enrollment_completion_page_configuration_policy_set_item import Windows10EnrollmentCompletionPageConfigurationPolicySetItem
				return Windows10EnrollmentCompletionPageConfigurationPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAutopilotDeploymentProfilePolicySetItem":
				from .windows_autopilot_deployment_profile_policy_set_item import WindowsAutopilotDeploymentProfilePolicySetItem
				return WindowsAutopilotDeploymentProfilePolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.policyTemplate":
				from .policy_template import PolicyTemplate
				return PolicyTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.presence":
				from .presence import Presence
				return Presence.model_validate(data)
			if mapping_key == "#microsoft.graph.presentation":
				from .presentation import Presentation
				return Presentation.model_validate(data)
			if mapping_key == "#microsoft.graph.printConnector":
				from .print_connector import PrintConnector
				return PrintConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.printDocument":
				from .print_document import PrintDocument
				return PrintDocument.model_validate(data)
			if mapping_key == "#microsoft.graph.printerBase":
				from .printer_base import PrinterBase
				return PrinterBase.model_validate(data)
			if mapping_key == "#microsoft.graph.printer":
				from .printer import Printer
				return Printer.model_validate(data)
			if mapping_key == "#microsoft.graph.printerShare":
				from .printer_share import PrinterShare
				return PrinterShare.model_validate(data)
			if mapping_key == "#microsoft.graph.printJob":
				from .print_job import PrintJob
				return PrintJob.model_validate(data)
			if mapping_key == "#microsoft.graph.printOperation":
				from .print_operation import PrintOperation
				return PrintOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.printerCreateOperation":
				from .printer_create_operation import PrinterCreateOperation
				return PrinterCreateOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.printService":
				from .print_service import PrintService
				return PrintService.model_validate(data)
			if mapping_key == "#microsoft.graph.printServiceEndpoint":
				from .print_service_endpoint import PrintServiceEndpoint
				return PrintServiceEndpoint.model_validate(data)
			if mapping_key == "#microsoft.graph.printTask":
				from .print_task import PrintTask
				return PrintTask.model_validate(data)
			if mapping_key == "#microsoft.graph.printTaskDefinition":
				from .print_task_definition import PrintTaskDefinition
				return PrintTaskDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.printTaskTrigger":
				from .print_task_trigger import PrintTaskTrigger
				return PrintTaskTrigger.model_validate(data)
			if mapping_key == "#microsoft.graph.printUsage":
				from .print_usage import PrintUsage
				return PrintUsage.model_validate(data)
			if mapping_key == "#microsoft.graph.printUsageByPrinter":
				from .print_usage_by_printer import PrintUsageByPrinter
				return PrintUsageByPrinter.model_validate(data)
			if mapping_key == "#microsoft.graph.printUsageByUser":
				from .print_usage_by_user import PrintUsageByUser
				return PrintUsageByUser.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccess":
				from .privileged_access import PrivilegedAccess
				return PrivilegedAccess.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessGroup":
				from .privileged_access_group import PrivilegedAccessGroup
				return PrivilegedAccessGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessRoot":
				from .privileged_access_root import PrivilegedAccessRoot
				return PrivilegedAccessRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessSchedule":
				from .privileged_access_schedule import PrivilegedAccessSchedule
				return PrivilegedAccessSchedule.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessGroupAssignmentSchedule":
				from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
				return PrivilegedAccessGroupAssignmentSchedule.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessGroupEligibilitySchedule":
				from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
				return PrivilegedAccessGroupEligibilitySchedule.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessScheduleInstance":
				from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance
				return PrivilegedAccessScheduleInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleInstance":
				from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
				return PrivilegedAccessGroupAssignmentScheduleInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleInstance":
				from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
				return PrivilegedAccessGroupEligibilityScheduleInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedApproval":
				from .privileged_approval import PrivilegedApproval
				return PrivilegedApproval.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedOperationEvent":
				from .privileged_operation_event import PrivilegedOperationEvent
				return PrivilegedOperationEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedRole":
				from .privileged_role import PrivilegedRole
				return PrivilegedRole.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedRoleAssignment":
				from .privileged_role_assignment import PrivilegedRoleAssignment
				return PrivilegedRoleAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedRoleAssignmentRequest":
				from .privileged_role_assignment_request import PrivilegedRoleAssignmentRequest
				return PrivilegedRoleAssignmentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedRoleSettings":
				from .privileged_role_settings import PrivilegedRoleSettings
				return PrivilegedRoleSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedRoleSummary":
				from .privileged_role_summary import PrivilegedRoleSummary
				return PrivilegedRoleSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedSignupStatus":
				from .privileged_signup_status import PrivilegedSignupStatus
				return PrivilegedSignupStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalation":
				from .privilege_escalation import PrivilegeEscalation
				return PrivilegeEscalation.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeManagementElevation":
				from .privilege_management_elevation import PrivilegeManagementElevation
				return PrivilegeManagementElevation.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeManagementElevationRequest":
				from .privilege_management_elevation_request import PrivilegeManagementElevationRequest
				return PrivilegeManagementElevationRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.profile":
				from .profile import Profile
				return Profile.model_validate(data)
			if mapping_key == "#microsoft.graph.profileCardProperty":
				from .profile_card_property import ProfileCardProperty
				return ProfileCardProperty.model_validate(data)
			if mapping_key == "#microsoft.graph.profilePhoto":
				from .profile_photo import ProfilePhoto
				return ProfilePhoto.model_validate(data)
			if mapping_key == "#microsoft.graph.profileSource":
				from .profile_source import ProfileSource
				return ProfileSource.model_validate(data)
			if mapping_key == "#microsoft.graph.program":
				from .program import Program
				return Program.model_validate(data)
			if mapping_key == "#microsoft.graph.programControl":
				from .program_control import ProgramControl
				return ProgramControl.model_validate(data)
			if mapping_key == "#microsoft.graph.programControlType":
				from .program_control_type import ProgramControlType
				return ProgramControlType.model_validate(data)
			if mapping_key == "#microsoft.graph.pronounsSettings":
				from .pronouns_settings import PronounsSettings
				return PronounsSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.protectionPolicyBase":
				from .protection_policy_base import ProtectionPolicyBase
				return ProtectionPolicyBase.model_validate(data)
			if mapping_key == "#microsoft.graph.exchangeProtectionPolicy":
				from .exchange_protection_policy import ExchangeProtectionPolicy
				return ExchangeProtectionPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.oneDriveForBusinessProtectionPolicy":
				from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
				return OneDriveForBusinessProtectionPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.sharePointProtectionPolicy":
				from .share_point_protection_policy import SharePointProtectionPolicy
				return SharePointProtectionPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.protectionRuleBase":
				from .protection_rule_base import ProtectionRuleBase
				return ProtectionRuleBase.model_validate(data)
			if mapping_key == "#microsoft.graph.driveProtectionRule":
				from .drive_protection_rule import DriveProtectionRule
				return DriveProtectionRule.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxProtectionRule":
				from .mailbox_protection_rule import MailboxProtectionRule
				return MailboxProtectionRule.model_validate(data)
			if mapping_key == "#microsoft.graph.siteProtectionRule":
				from .site_protection_rule import SiteProtectionRule
				return SiteProtectionRule.model_validate(data)
			if mapping_key == "#microsoft.graph.protectionUnitBase":
				from .protection_unit_base import ProtectionUnitBase
				return ProtectionUnitBase.model_validate(data)
			if mapping_key == "#microsoft.graph.driveProtectionUnit":
				from .drive_protection_unit import DriveProtectionUnit
				return DriveProtectionUnit.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxProtectionUnit":
				from .mailbox_protection_unit import MailboxProtectionUnit
				return MailboxProtectionUnit.model_validate(data)
			if mapping_key == "#microsoft.graph.siteProtectionUnit":
				from .site_protection_unit import SiteProtectionUnit
				return SiteProtectionUnit.model_validate(data)
			if mapping_key == "#microsoft.graph.protectionUnitsBulkJobBase":
				from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase
				return ProtectionUnitsBulkJobBase.model_validate(data)
			if mapping_key == "#microsoft.graph.driveProtectionUnitsBulkAdditionJob":
				from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
				return DriveProtectionUnitsBulkAdditionJob.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxProtectionUnitsBulkAdditionJob":
				from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob
				return MailboxProtectionUnitsBulkAdditionJob.model_validate(data)
			if mapping_key == "#microsoft.graph.siteProtectionUnitsBulkAdditionJob":
				from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob
				return SiteProtectionUnitsBulkAdditionJob.model_validate(data)
			if mapping_key == "#microsoft.graph.providerTenantSetting":
				from .provider_tenant_setting import ProviderTenantSetting
				return ProviderTenantSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.provisioningObjectSummary":
				from .provisioning_object_summary import ProvisioningObjectSummary
				return ProvisioningObjectSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.publicKeyInfrastructureRoot":
				from .public_key_infrastructure_root import PublicKeyInfrastructureRoot
				return PublicKeyInfrastructureRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.publishedResource":
				from .published_resource import PublishedResource
				return PublishedResource.model_validate(data)
			if mapping_key == "#microsoft.graph.purchaseInvoiceLine":
				from .purchase_invoice_line import PurchaseInvoiceLine
				return PurchaseInvoiceLine.model_validate(data)
			if mapping_key == "#microsoft.graph.rbacApplication":
				from .rbac_application import RbacApplication
				return RbacApplication.model_validate(data)
			if mapping_key == "#microsoft.graph.rbacApplicationMultiple":
				from .rbac_application_multiple import RbacApplicationMultiple
				return RbacApplicationMultiple.model_validate(data)
			if mapping_key == "#microsoft.graph.readingAssignmentSubmission":
				from .reading_assignment_submission import ReadingAssignmentSubmission
				return ReadingAssignmentSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.recommendationBase":
				from .recommendation_base import RecommendationBase
				return RecommendationBase.model_validate(data)
			if mapping_key == "#microsoft.graph.recommendation":
				from .recommendation import Recommendation
				return Recommendation.model_validate(data)
			if mapping_key == "#microsoft.graph.reflectCheckInResponse":
				from .reflect_check_in_response import ReflectCheckInResponse
				return ReflectCheckInResponse.model_validate(data)
			if mapping_key == "#microsoft.graph.regionalAndLanguageSettings":
				from .regional_and_language_settings import RegionalAndLanguageSettings
				return RegionalAndLanguageSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.relyingPartyDetailedSummary":
				from .relying_party_detailed_summary import RelyingPartyDetailedSummary
				return RelyingPartyDetailedSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.remoteActionAudit":
				from .remote_action_audit import RemoteActionAudit
				return RemoteActionAudit.model_validate(data)
			if mapping_key == "#microsoft.graph.remoteAssistancePartner":
				from .remote_assistance_partner import RemoteAssistancePartner
				return RemoteAssistancePartner.model_validate(data)
			if mapping_key == "#microsoft.graph.remoteAssistanceSettings":
				from .remote_assistance_settings import RemoteAssistanceSettings
				return RemoteAssistanceSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.remoteDesktopSecurityConfiguration":
				from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
				return RemoteDesktopSecurityConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.reportRoot":
				from .report_root import ReportRoot
				return ReportRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.reportsRoot":
				from .reports_root import ReportsRoot
				return ReportsRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.request":
				from .request import Request
				return Request.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessScheduleRequest":
				from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest
				return PrivilegedAccessScheduleRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleRequest":
				from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
				return PrivilegedAccessGroupAssignmentScheduleRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest":
				from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
				return PrivilegedAccessGroupEligibilityScheduleRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleAssignmentScheduleRequest":
				from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
				return UnifiedRoleAssignmentScheduleRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleEligibilityScheduleRequest":
				from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
				return UnifiedRoleEligibilityScheduleRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.userConsentRequest":
				from .user_consent_request import UserConsentRequest
				return UserConsentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.resourceOperation":
				from .resource_operation import ResourceOperation
				return ResourceOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.restoreArtifactBase":
				from .restore_artifact_base import RestoreArtifactBase
				return RestoreArtifactBase.model_validate(data)
			if mapping_key == "#microsoft.graph.driveRestoreArtifact":
				from .drive_restore_artifact import DriveRestoreArtifact
				return DriveRestoreArtifact.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxRestoreArtifact":
				from .mailbox_restore_artifact import MailboxRestoreArtifact
				return MailboxRestoreArtifact.model_validate(data)
			if mapping_key == "#microsoft.graph.granularMailboxRestoreArtifact":
				from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
				return GranularMailboxRestoreArtifact.model_validate(data)
			if mapping_key == "#microsoft.graph.siteRestoreArtifact":
				from .site_restore_artifact import SiteRestoreArtifact
				return SiteRestoreArtifact.model_validate(data)
			if mapping_key == "#microsoft.graph.restoreArtifactsBulkRequestBase":
				from .restore_artifacts_bulk_request_base import RestoreArtifactsBulkRequestBase
				return RestoreArtifactsBulkRequestBase.model_validate(data)
			if mapping_key == "#microsoft.graph.driveRestoreArtifactsBulkAdditionRequest":
				from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
				return DriveRestoreArtifactsBulkAdditionRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxRestoreArtifactsBulkAdditionRequest":
				from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest
				return MailboxRestoreArtifactsBulkAdditionRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.siteRestoreArtifactsBulkAdditionRequest":
				from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest
				return SiteRestoreArtifactsBulkAdditionRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.restorePoint":
				from .restore_point import RestorePoint
				return RestorePoint.model_validate(data)
			if mapping_key == "#microsoft.graph.restoreSessionBase":
				from .restore_session_base import RestoreSessionBase
				return RestoreSessionBase.model_validate(data)
			if mapping_key == "#microsoft.graph.exchangeRestoreSession":
				from .exchange_restore_session import ExchangeRestoreSession
				return ExchangeRestoreSession.model_validate(data)
			if mapping_key == "#microsoft.graph.oneDriveForBusinessRestoreSession":
				from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
				return OneDriveForBusinessRestoreSession.model_validate(data)
			if mapping_key == "#microsoft.graph.sharePointRestoreSession":
				from .share_point_restore_session import SharePointRestoreSession
				return SharePointRestoreSession.model_validate(data)
			if mapping_key == "#microsoft.graph.restrictedAppsViolation":
				from .restricted_apps_violation import RestrictedAppsViolation
				return RestrictedAppsViolation.model_validate(data)
			if mapping_key == "#microsoft.graph.riskDetection":
				from .risk_detection import RiskDetection
				return RiskDetection.model_validate(data)
			if mapping_key == "#microsoft.graph.riskyServicePrincipal":
				from .risky_service_principal import RiskyServicePrincipal
				return RiskyServicePrincipal.model_validate(data)
			if mapping_key == "#microsoft.graph.riskyServicePrincipalHistoryItem":
				from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
				return RiskyServicePrincipalHistoryItem.model_validate(data)
			if mapping_key == "#microsoft.graph.riskyUser":
				from .risky_user import RiskyUser
				return RiskyUser.model_validate(data)
			if mapping_key == "#microsoft.graph.riskyUserHistoryItem":
				from .risky_user_history_item import RiskyUserHistoryItem
				return RiskyUserHistoryItem.model_validate(data)
			if mapping_key == "#microsoft.graph.roleAssignment":
				from .role_assignment import RoleAssignment
				return RoleAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceAndAppManagementRoleAssignment":
				from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
				return DeviceAndAppManagementRoleAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.roleDefinition":
				from .role_definition import RoleDefinition
				return RoleDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceAndAppManagementRoleDefinition":
				from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
				return DeviceAndAppManagementRoleDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.roleManagementAlert":
				from .role_management_alert import RoleManagementAlert
				return RoleManagementAlert.model_validate(data)
			if mapping_key == "#microsoft.graph.roleScopeTag":
				from .role_scope_tag import RoleScopeTag
				return RoleScopeTag.model_validate(data)
			if mapping_key == "#microsoft.graph.roleScopeTagAutoAssignment":
				from .role_scope_tag_auto_assignment import RoleScopeTagAutoAssignment
				return RoleScopeTagAutoAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.salesCreditMemoLine":
				from .sales_credit_memo_line import SalesCreditMemoLine
				return SalesCreditMemoLine.model_validate(data)
			if mapping_key == "#microsoft.graph.salesInvoiceLine":
				from .sales_invoice_line import SalesInvoiceLine
				return SalesInvoiceLine.model_validate(data)
			if mapping_key == "#microsoft.graph.salesOrderLine":
				from .sales_order_line import SalesOrderLine
				return SalesOrderLine.model_validate(data)
			if mapping_key == "#microsoft.graph.salesQuoteLine":
				from .sales_quote_line import SalesQuoteLine
				return SalesQuoteLine.model_validate(data)
			if mapping_key == "#microsoft.graph.schedule":
				from .schedule import Schedule
				return Schedule.model_validate(data)
			if mapping_key == "#microsoft.graph.scheduledPermissionsRequest":
				from .scheduled_permissions_request import ScheduledPermissionsRequest
				return ScheduledPermissionsRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.schema":
				from .schema import Schema
				return Schema.model_validate(data)
			if mapping_key == "#microsoft.graph.schemaExtension":
				from .schema_extension import SchemaExtension
				return SchemaExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.scopedRoleMembership":
				from .scoped_role_membership import ScopedRoleMembership
				return ScopedRoleMembership.model_validate(data)
			if mapping_key == "#microsoft.graph.searchEntity":
				from .search_entity import SearchEntity
				return SearchEntity.model_validate(data)
			if mapping_key == "#microsoft.graph.secureScore":
				from .secure_score import SecureScore
				return SecureScore.model_validate(data)
			if mapping_key == "#microsoft.graph.secureScoreControlProfile":
				from .secure_score_control_profile import SecureScoreControlProfile
				return SecureScoreControlProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.securityAction":
				from .security_action import SecurityAction
				return SecurityAction.model_validate(data)
			if mapping_key == "#microsoft.graph.securityBaselineDeviceState":
				from .security_baseline_device_state import SecurityBaselineDeviceState
				return SecurityBaselineDeviceState.model_validate(data)
			if mapping_key == "#microsoft.graph.securityBaselineSettingState":
				from .security_baseline_setting_state import SecurityBaselineSettingState
				return SecurityBaselineSettingState.model_validate(data)
			if mapping_key == "#microsoft.graph.securityBaselineState":
				from .security_baseline_state import SecurityBaselineState
				return SecurityBaselineState.model_validate(data)
			if mapping_key == "#microsoft.graph.securityBaselineStateSummary":
				from .security_baseline_state_summary import SecurityBaselineStateSummary
				return SecurityBaselineStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.securityBaselineCategoryStateSummary":
				from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary
				return SecurityBaselineCategoryStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.securityReportsRoot":
				from .security_reports_root import SecurityReportsRoot
				return SecurityReportsRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.selfServiceSignUp":
				from .self_service_sign_up import SelfServiceSignUp
				return SelfServiceSignUp.model_validate(data)
			if mapping_key == "#microsoft.graph.sensitiveType":
				from .sensitive_type import SensitiveType
				return SensitiveType.model_validate(data)
			if mapping_key == "#microsoft.graph.sensitivityLabel":
				from .sensitivity_label import SensitivityLabel
				return SensitivityLabel.model_validate(data)
			if mapping_key == "#microsoft.graph.sensitivityPolicySettings":
				from .sensitivity_policy_settings import SensitivityPolicySettings
				return SensitivityPolicySettings.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceActivity":
				from .service_activity import ServiceActivity
				return ServiceActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceAnnouncement":
				from .service_announcement import ServiceAnnouncement
				return ServiceAnnouncement.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceAnnouncementAttachment":
				from .service_announcement_attachment import ServiceAnnouncementAttachment
				return ServiceAnnouncementAttachment.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceAnnouncementBase":
				from .service_announcement_base import ServiceAnnouncementBase
				return ServiceAnnouncementBase.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceHealthIssue":
				from .service_health_issue import ServiceHealthIssue
				return ServiceHealthIssue.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceUpdateMessage":
				from .service_update_message import ServiceUpdateMessage
				return ServiceUpdateMessage.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceApp":
				from .service_app import ServiceApp
				return ServiceApp.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceHealth":
				from .service_health import ServiceHealth
				return ServiceHealth.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceLevelAgreementRoot":
				from .service_level_agreement_root import ServiceLevelAgreementRoot
				return ServiceLevelAgreementRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceNowConnection":
				from .service_now_connection import ServiceNowConnection
				return ServiceNowConnection.model_validate(data)
			if mapping_key == "#microsoft.graph.servicePrincipalCreationConditionSet":
				from .service_principal_creation_condition_set import ServicePrincipalCreationConditionSet
				return ServicePrincipalCreationConditionSet.model_validate(data)
			if mapping_key == "#microsoft.graph.servicePrincipalRiskDetection":
				from .service_principal_risk_detection import ServicePrincipalRiskDetection
				return ServicePrincipalRiskDetection.model_validate(data)
			if mapping_key == "#microsoft.graph.servicePrincipalSignInActivity":
				from .service_principal_sign_in_activity import ServicePrincipalSignInActivity
				return ServicePrincipalSignInActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.settingStateDeviceSummary":
				from .setting_state_device_summary import SettingStateDeviceSummary
				return SettingStateDeviceSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedEmailDomain":
				from .shared_email_domain import SharedEmailDomain
				return SharedEmailDomain.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedEmailDomainInvitation":
				from .shared_email_domain_invitation import SharedEmailDomainInvitation
				return SharedEmailDomainInvitation.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedInsight":
				from .shared_insight import SharedInsight
				return SharedInsight.model_validate(data)
			if mapping_key == "#microsoft.graph.sharepoint":
				from .sharepoint import Sharepoint
				return Sharepoint.model_validate(data)
			if mapping_key == "#microsoft.graph.sharepointSettings":
				from .sharepoint_settings import SharepointSettings
				return SharepointSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.shiftsRoleDefinition":
				from .shifts_role_definition import ShiftsRoleDefinition
				return ShiftsRoleDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.signIn":
				from .sign_in import SignIn
				return SignIn.model_validate(data)
			if mapping_key == "#microsoft.graph.simulation":
				from .simulation import Simulation
				return Simulation.model_validate(data)
			if mapping_key == "#microsoft.graph.simulationAutomation":
				from .simulation_automation import SimulationAutomation
				return SimulationAutomation.model_validate(data)
			if mapping_key == "#microsoft.graph.simulationAutomationRun":
				from .simulation_automation_run import SimulationAutomationRun
				return SimulationAutomationRun.model_validate(data)
			if mapping_key == "#microsoft.graph.singleValueLegacyExtendedProperty":
				from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
				return SingleValueLegacyExtendedProperty.model_validate(data)
			if mapping_key == "#microsoft.graph.softwareUpdateStatusSummary":
				from .software_update_status_summary import SoftwareUpdateStatusSummary
				return SoftwareUpdateStatusSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.storageQuotaBreakdown":
				from .storage_quota_breakdown import StorageQuotaBreakdown
				return StorageQuotaBreakdown.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceStorageQuotaBreakdown":
				from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown
				return ServiceStorageQuotaBreakdown.model_validate(data)
			if mapping_key == "#microsoft.graph.storageSettings":
				from .storage_settings import StorageSettings
				return StorageSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.strongAuthenticationDetail":
				from .strong_authentication_detail import StrongAuthenticationDetail
				return StrongAuthenticationDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.strongAuthenticationPhoneAppDetail":
				from .strong_authentication_phone_app_detail import StrongAuthenticationPhoneAppDetail
				return StrongAuthenticationPhoneAppDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.subjectRightsRequest":
				from .subject_rights_request import SubjectRightsRequest
				return SubjectRightsRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.subscribedSku":
				from .subscribed_sku import SubscribedSku
				return SubscribedSku.model_validate(data)
			if mapping_key == "#microsoft.graph.subscription":
				from .subscription import Subscription
				return Subscription.model_validate(data)
			if mapping_key == "#microsoft.graph.symantecCodeSigningCertificate":
				from .symantec_code_signing_certificate import SymantecCodeSigningCertificate
				return SymantecCodeSigningCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.synchronization":
				from .synchronization import Synchronization
				return Synchronization.model_validate(data)
			if mapping_key == "#microsoft.graph.synchronizationJob":
				from .synchronization_job import SynchronizationJob
				return SynchronizationJob.model_validate(data)
			if mapping_key == "#microsoft.graph.synchronizationSchema":
				from .synchronization_schema import SynchronizationSchema
				return SynchronizationSchema.model_validate(data)
			if mapping_key == "#microsoft.graph.synchronizationTemplate":
				from .synchronization_template import SynchronizationTemplate
				return SynchronizationTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.targetDeviceGroup":
				from .target_device_group import TargetDeviceGroup
				return TargetDeviceGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.targetedManagedAppPolicyAssignment":
				from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
				return TargetedManagedAppPolicyAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.taxGroup":
				from .tax_group import TaxGroup
				return TaxGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.team":
				from .team import Team
				return Team.model_validate(data)
			if mapping_key == "#microsoft.graph.teamInfo":
				from .team_info import TeamInfo
				return TeamInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.associatedTeamInfo":
				from .associated_team_info import AssociatedTeamInfo
				return AssociatedTeamInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedWithChannelTeamInfo":
				from .shared_with_channel_team_info import SharedWithChannelTeamInfo
				return SharedWithChannelTeamInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsApp":
				from .teams_app import TeamsApp
				return TeamsApp.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsAppDashboardCardDefinition":
				from .teams_app_dashboard_card_definition import TeamsAppDashboardCardDefinition
				return TeamsAppDashboardCardDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsAppDefinition":
				from .teams_app_definition import TeamsAppDefinition
				return TeamsAppDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsAppIcon":
				from .teams_app_icon import TeamsAppIcon
				return TeamsAppIcon.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsAppInstallation":
				from .teams_app_installation import TeamsAppInstallation
				return TeamsAppInstallation.model_validate(data)
			if mapping_key == "#microsoft.graph.userScopeTeamsAppInstallation":
				from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation
				return UserScopeTeamsAppInstallation.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsAppSettings":
				from .teams_app_settings import TeamsAppSettings
				return TeamsAppSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsAsyncOperation":
				from .teams_async_operation import TeamsAsyncOperation
				return TeamsAsyncOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsChannelPlanner":
				from .teams_channel_planner import TeamsChannelPlanner
				return TeamsChannelPlanner.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsTab":
				from .teams_tab import TeamsTab
				return TeamsTab.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsTemplate":
				from .teams_template import TeamsTemplate
				return TeamsTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.teamTemplate":
				from .team_template import TeamTemplate
				return TeamTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.teamTemplateDefinition":
				from .team_template_definition import TeamTemplateDefinition
				return TeamTemplateDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.teamwork":
				from .teamwork import Teamwork
				return Teamwork.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkBot":
				from .teamwork_bot import TeamworkBot
				return TeamworkBot.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkDevice":
				from .teamwork_device import TeamworkDevice
				return TeamworkDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkDeviceActivity":
				from .teamwork_device_activity import TeamworkDeviceActivity
				return TeamworkDeviceActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkDeviceConfiguration":
				from .teamwork_device_configuration import TeamworkDeviceConfiguration
				return TeamworkDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkDeviceHealth":
				from .teamwork_device_health import TeamworkDeviceHealth
				return TeamworkDeviceHealth.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkDeviceOperation":
				from .teamwork_device_operation import TeamworkDeviceOperation
				return TeamworkDeviceOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkHostedContent":
				from .teamwork_hosted_content import TeamworkHostedContent
				return TeamworkHostedContent.model_validate(data)
			if mapping_key == "#microsoft.graph.chatMessageHostedContent":
				from .chat_message_hosted_content import ChatMessageHostedContent
				return ChatMessageHostedContent.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkPeripheral":
				from .teamwork_peripheral import TeamworkPeripheral
				return TeamworkPeripheral.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkTag":
				from .teamwork_tag import TeamworkTag
				return TeamworkTag.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkTagMember":
				from .teamwork_tag_member import TeamworkTagMember
				return TeamworkTagMember.model_validate(data)
			if mapping_key == "#microsoft.graph.telecomExpenseManagementPartner":
				from .telecom_expense_management_partner import TelecomExpenseManagementPartner
				return TelecomExpenseManagementPartner.model_validate(data)
			if mapping_key == "#microsoft.graph.template":
				from .template import Template
				return Template.model_validate(data)
			if mapping_key == "#microsoft.graph.tenantAttachRBAC":
				from .tenant_attach_r_b_a_c import TenantAttachRBAC
				return TenantAttachRBAC.model_validate(data)
			if mapping_key == "#microsoft.graph.tenantSetupInfo":
				from .tenant_setup_info import TenantSetupInfo
				return TenantSetupInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.termsAndConditions":
				from .terms_and_conditions import TermsAndConditions
				return TermsAndConditions.model_validate(data)
			if mapping_key == "#microsoft.graph.termsAndConditionsAcceptanceStatus":
				from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
				return TermsAndConditionsAcceptanceStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.termsAndConditionsAssignment":
				from .terms_and_conditions_assignment import TermsAndConditionsAssignment
				return TermsAndConditionsAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.termsAndConditionsGroupAssignment":
				from .terms_and_conditions_group_assignment import TermsAndConditionsGroupAssignment
				return TermsAndConditionsGroupAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.termsOfUseContainer":
				from .terms_of_use_container import TermsOfUseContainer
				return TermsOfUseContainer.model_validate(data)
			if mapping_key == "#microsoft.graph.textClassificationRequest":
				from .text_classification_request import TextClassificationRequest
				return TextClassificationRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.threatAssessmentRequest":
				from .threat_assessment_request import ThreatAssessmentRequest
				return ThreatAssessmentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.emailFileAssessmentRequest":
				from .email_file_assessment_request import EmailFileAssessmentRequest
				return EmailFileAssessmentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.fileAssessmentRequest":
				from .file_assessment_request import FileAssessmentRequest
				return FileAssessmentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.mailAssessmentRequest":
				from .mail_assessment_request import MailAssessmentRequest
				return MailAssessmentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.urlAssessmentRequest":
				from .url_assessment_request import UrlAssessmentRequest
				return UrlAssessmentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.threatAssessmentResult":
				from .threat_assessment_result import ThreatAssessmentResult
				return ThreatAssessmentResult.model_validate(data)
			if mapping_key == "#microsoft.graph.thumbnailSet":
				from .thumbnail_set import ThumbnailSet
				return ThumbnailSet.model_validate(data)
			if mapping_key == "#microsoft.graph.tiIndicator":
				from .ti_indicator import TiIndicator
				return TiIndicator.model_validate(data)
			if mapping_key == "#microsoft.graph.todo":
				from .todo import Todo
				return Todo.model_validate(data)
			if mapping_key == "#microsoft.graph.todoTask":
				from .todo_task import TodoTask
				return TodoTask.model_validate(data)
			if mapping_key == "#microsoft.graph.todoTaskList":
				from .todo_task_list import TodoTaskList
				return TodoTaskList.model_validate(data)
			if mapping_key == "#microsoft.graph.training":
				from .training import Training
				return Training.model_validate(data)
			if mapping_key == "#microsoft.graph.trainingCampaign":
				from .training_campaign import TrainingCampaign
				return TrainingCampaign.model_validate(data)
			if mapping_key == "#microsoft.graph.trainingLanguageDetail":
				from .training_language_detail import TrainingLanguageDetail
				return TrainingLanguageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.trending":
				from .trending import Trending
				return Trending.model_validate(data)
			if mapping_key == "#microsoft.graph.trustFrameworkKeySet":
				from .trust_framework_key_set import TrustFrameworkKeySet
				return TrustFrameworkKeySet.model_validate(data)
			if mapping_key == "#microsoft.graph.trustFrameworkPolicy":
				from .trust_framework_policy import TrustFrameworkPolicy
				return TrustFrameworkPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRbacApplication":
				from .unified_rbac_application import UnifiedRbacApplication
				return UnifiedRbacApplication.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRbacResourceAction":
				from .unified_rbac_resource_action import UnifiedRbacResourceAction
				return UnifiedRbacResourceAction.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRbacResourceNamespace":
				from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
				return UnifiedRbacResourceNamespace.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRbacResourceScope":
				from .unified_rbac_resource_scope import UnifiedRbacResourceScope
				return UnifiedRbacResourceScope.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleAssignment":
				from .unified_role_assignment import UnifiedRoleAssignment
				return UnifiedRoleAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleAssignmentMultiple":
				from .unified_role_assignment_multiple import UnifiedRoleAssignmentMultiple
				return UnifiedRoleAssignmentMultiple.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleDefinition":
				from .unified_role_definition import UnifiedRoleDefinition
				return UnifiedRoleDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementAlert":
				from .unified_role_management_alert import UnifiedRoleManagementAlert
				return UnifiedRoleManagementAlert.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementAlertConfiguration":
				from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
				return UnifiedRoleManagementAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.invalidLicenseAlertConfiguration":
				from .invalid_license_alert_configuration import InvalidLicenseAlertConfiguration
				return InvalidLicenseAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.noMfaOnRoleActivationAlertConfiguration":
				from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration
				return NoMfaOnRoleActivationAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.redundantAssignmentAlertConfiguration":
				from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration
				return RedundantAssignmentAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration":
				from .roles_assigned_outside_privileged_identity_management_alert_configuration import RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration
				return RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.sequentialActivationRenewalsAlertConfiguration":
				from .sequential_activation_renewals_alert_configuration import SequentialActivationRenewalsAlertConfiguration
				return SequentialActivationRenewalsAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.staleSignInAlertConfiguration":
				from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration
				return StaleSignInAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertConfiguration":
				from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration
				return TooManyGlobalAdminsAssignedToTenantAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementAlertDefinition":
				from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition
				return UnifiedRoleManagementAlertDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementAlertIncident":
				from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident
				return UnifiedRoleManagementAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.invalidLicenseAlertIncident":
				from .invalid_license_alert_incident import InvalidLicenseAlertIncident
				return InvalidLicenseAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.noMfaOnRoleActivationAlertIncident":
				from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident
				return NoMfaOnRoleActivationAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.redundantAssignmentAlertIncident":
				from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident
				return RedundantAssignmentAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertIncident":
				from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident
				return RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.sequentialActivationRenewalsAlertIncident":
				from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident
				return SequentialActivationRenewalsAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.staleSignInAlertIncident":
				from .stale_sign_in_alert_incident import StaleSignInAlertIncident
				return StaleSignInAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertIncident":
				from .too_many_global_admins_assigned_to_tenant_alert_incident import TooManyGlobalAdminsAssignedToTenantAlertIncident
				return TooManyGlobalAdminsAssignedToTenantAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicy":
				from .unified_role_management_policy import UnifiedRoleManagementPolicy
				return UnifiedRoleManagementPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicyAssignment":
				from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment
				return UnifiedRoleManagementPolicyAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicyRule":
				from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule
				return UnifiedRoleManagementPolicyRule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule":
				from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
				return UnifiedRoleManagementPolicyApprovalRule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule":
				from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
				return UnifiedRoleManagementPolicyAuthenticationContextRule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule":
				from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
				return UnifiedRoleManagementPolicyEnablementRule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule":
				from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
				return UnifiedRoleManagementPolicyExpirationRule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule":
				from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule
				return UnifiedRoleManagementPolicyNotificationRule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleScheduleBase":
				from .unified_role_schedule_base import UnifiedRoleScheduleBase
				return UnifiedRoleScheduleBase.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleAssignmentSchedule":
				from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
				return UnifiedRoleAssignmentSchedule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleEligibilitySchedule":
				from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
				return UnifiedRoleEligibilitySchedule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleScheduleInstanceBase":
				from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase
				return UnifiedRoleScheduleInstanceBase.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleAssignmentScheduleInstance":
				from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
				return UnifiedRoleAssignmentScheduleInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleEligibilityScheduleInstance":
				from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
				return UnifiedRoleEligibilityScheduleInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedStorageQuota":
				from .unified_storage_quota import UnifiedStorageQuota
				return UnifiedStorageQuota.model_validate(data)
			if mapping_key == "#microsoft.graph.unsupportedGroupPolicyExtension":
				from .unsupported_group_policy_extension import UnsupportedGroupPolicyExtension
				return UnsupportedGroupPolicyExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.usageRight":
				from .usage_right import UsageRight
				return UsageRight.model_validate(data)
			if mapping_key == "#microsoft.graph.usedInsight":
				from .used_insight import UsedInsight
				return UsedInsight.model_validate(data)
			if mapping_key == "#microsoft.graph.userActivity":
				from .user_activity import UserActivity
				return UserActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.userAnalytics":
				from .user_analytics import UserAnalytics
				return UserAnalytics.model_validate(data)
			if mapping_key == "#microsoft.graph.userAppInstallStatus":
				from .user_app_install_status import UserAppInstallStatus
				return UserAppInstallStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.userConfiguration":
				from .user_configuration import UserConfiguration
				return UserConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.userCountMetric":
				from .user_count_metric import UserCountMetric
				return UserCountMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.userCredentialUsageDetails":
				from .user_credential_usage_details import UserCredentialUsageDetails
				return UserCredentialUsageDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAnomaly":
				from .user_experience_analytics_anomaly import UserExperienceAnalyticsAnomaly
				return UserExperienceAnalyticsAnomaly.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAnomalyCorrelationGroupOverview":
				from .user_experience_analytics_anomaly_correlation_group_overview import UserExperienceAnalyticsAnomalyCorrelationGroupOverview
				return UserExperienceAnalyticsAnomalyCorrelationGroupOverview.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAnomalyDevice":
				from .user_experience_analytics_anomaly_device import UserExperienceAnalyticsAnomalyDevice
				return UserExperienceAnalyticsAnomalyDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAppHealthApplicationPerformance":
				from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
				return UserExperienceAnalyticsAppHealthApplicationPerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByAppVersion":
				from .user_experience_analytics_app_health_app_performance_by_app_version import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion
				return UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails":
				from .user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
				return UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId":
				from .user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
				return UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByOSVersion":
				from .user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
				return UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAppHealthDeviceModelPerformance":
				from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance
				return UserExperienceAnalyticsAppHealthDeviceModelPerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAppHealthDevicePerformance":
				from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance
				return UserExperienceAnalyticsAppHealthDevicePerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAppHealthDevicePerformanceDetails":
				from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails
				return UserExperienceAnalyticsAppHealthDevicePerformanceDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAppHealthOSVersionPerformance":
				from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance
				return UserExperienceAnalyticsAppHealthOSVersionPerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsBaseline":
				from .user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
				return UserExperienceAnalyticsBaseline.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsBatteryHealthAppImpact":
				from .user_experience_analytics_battery_health_app_impact import UserExperienceAnalyticsBatteryHealthAppImpact
				return UserExperienceAnalyticsBatteryHealthAppImpact.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsBatteryHealthCapacityDetails":
				from .user_experience_analytics_battery_health_capacity_details import UserExperienceAnalyticsBatteryHealthCapacityDetails
				return UserExperienceAnalyticsBatteryHealthCapacityDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsBatteryHealthDeviceAppImpact":
				from .user_experience_analytics_battery_health_device_app_impact import UserExperienceAnalyticsBatteryHealthDeviceAppImpact
				return UserExperienceAnalyticsBatteryHealthDeviceAppImpact.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsBatteryHealthDevicePerformance":
				from .user_experience_analytics_battery_health_device_performance import UserExperienceAnalyticsBatteryHealthDevicePerformance
				return UserExperienceAnalyticsBatteryHealthDevicePerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory":
				from .user_experience_analytics_battery_health_device_runtime_history import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory
				return UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsBatteryHealthModelPerformance":
				from .user_experience_analytics_battery_health_model_performance import UserExperienceAnalyticsBatteryHealthModelPerformance
				return UserExperienceAnalyticsBatteryHealthModelPerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsBatteryHealthOsPerformance":
				from .user_experience_analytics_battery_health_os_performance import UserExperienceAnalyticsBatteryHealthOsPerformance
				return UserExperienceAnalyticsBatteryHealthOsPerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsBatteryHealthRuntimeDetails":
				from .user_experience_analytics_battery_health_runtime_details import UserExperienceAnalyticsBatteryHealthRuntimeDetails
				return UserExperienceAnalyticsBatteryHealthRuntimeDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsCategory":
				from .user_experience_analytics_category import UserExperienceAnalyticsCategory
				return UserExperienceAnalyticsCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsDevicePerformance":
				from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
				return UserExperienceAnalyticsDevicePerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsDeviceScope":
				from .user_experience_analytics_device_scope import UserExperienceAnalyticsDeviceScope
				return UserExperienceAnalyticsDeviceScope.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsDeviceScores":
				from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores
				return UserExperienceAnalyticsDeviceScores.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsDeviceStartupHistory":
				from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory
				return UserExperienceAnalyticsDeviceStartupHistory.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsDeviceStartupProcess":
				from .user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess
				return UserExperienceAnalyticsDeviceStartupProcess.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsDeviceStartupProcessPerformance":
				from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance
				return UserExperienceAnalyticsDeviceStartupProcessPerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsDeviceTimelineEvent":
				from .user_experience_analytics_device_timeline_event import UserExperienceAnalyticsDeviceTimelineEvent
				return UserExperienceAnalyticsDeviceTimelineEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsDeviceWithoutCloudIdentity":
				from .user_experience_analytics_device_without_cloud_identity import UserExperienceAnalyticsDeviceWithoutCloudIdentity
				return UserExperienceAnalyticsDeviceWithoutCloudIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsImpactingProcess":
				from .user_experience_analytics_impacting_process import UserExperienceAnalyticsImpactingProcess
				return UserExperienceAnalyticsImpactingProcess.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsMetric":
				from .user_experience_analytics_metric import UserExperienceAnalyticsMetric
				return UserExperienceAnalyticsMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsMetricHistory":
				from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
				return UserExperienceAnalyticsMetricHistory.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsModelScores":
				from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
				return UserExperienceAnalyticsModelScores.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsNotAutopilotReadyDevice":
				from .user_experience_analytics_not_autopilot_ready_device import UserExperienceAnalyticsNotAutopilotReadyDevice
				return UserExperienceAnalyticsNotAutopilotReadyDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsOverview":
				from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
				return UserExperienceAnalyticsOverview.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsRemoteConnection":
				from .user_experience_analytics_remote_connection import UserExperienceAnalyticsRemoteConnection
				return UserExperienceAnalyticsRemoteConnection.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsResourcePerformance":
				from .user_experience_analytics_resource_performance import UserExperienceAnalyticsResourcePerformance
				return UserExperienceAnalyticsResourcePerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsScoreHistory":
				from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
				return UserExperienceAnalyticsScoreHistory.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereDevice":
				from .user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice
				return UserExperienceAnalyticsWorkFromAnywhereDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric":
				from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
				return UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereMetric":
				from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
				return UserExperienceAnalyticsWorkFromAnywhereMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereModelPerformance":
				from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
				return UserExperienceAnalyticsWorkFromAnywhereModelPerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.userFlowLanguageConfiguration":
				from .user_flow_language_configuration import UserFlowLanguageConfiguration
				return UserFlowLanguageConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.userFlowLanguagePage":
				from .user_flow_language_page import UserFlowLanguagePage
				return UserFlowLanguagePage.model_validate(data)
			if mapping_key == "#microsoft.graph.userInsightsRoot":
				from .user_insights_root import UserInsightsRoot
				return UserInsightsRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.userInsightsSettings":
				from .user_insights_settings import UserInsightsSettings
				return UserInsightsSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.userInstallStateSummary":
				from .user_install_state_summary import UserInstallStateSummary
				return UserInstallStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.userPFXCertificate":
				from .user_p_f_x_certificate import UserPFXCertificate
				return UserPFXCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.userRegistrationDetails":
				from .user_registration_details import UserRegistrationDetails
				return UserRegistrationDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.userRequestsMetric":
				from .user_requests_metric import UserRequestsMetric
				return UserRequestsMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.userSecurityProfile":
				from .user_security_profile import UserSecurityProfile
				return UserSecurityProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.userSettings":
				from .user_settings import UserSettings
				return UserSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.userSignUpMetric":
				from .user_sign_up_metric import UserSignUpMetric
				return UserSignUpMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.userSolutionRoot":
				from .user_solution_root import UserSolutionRoot
				return UserSolutionRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.userStorage":
				from .user_storage import UserStorage
				return UserStorage.model_validate(data)
			if mapping_key == "#microsoft.graph.userTeamwork":
				from .user_teamwork import UserTeamwork
				return UserTeamwork.model_validate(data)
			if mapping_key == "#microsoft.graph.userVirtualEventsRoot":
				from .user_virtual_events_root import UserVirtualEventsRoot
				return UserVirtualEventsRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.uxSetting":
				from .ux_setting import UxSetting
				return UxSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.verticalSection":
				from .vertical_section import VerticalSection
				return VerticalSection.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEndpoint":
				from .virtual_endpoint import VirtualEndpoint
				return VirtualEndpoint.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEvent":
				from .virtual_event import VirtualEvent
				return VirtualEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventTownhall":
				from .virtual_event_townhall import VirtualEventTownhall
				return VirtualEventTownhall.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventWebinar":
				from .virtual_event_webinar import VirtualEventWebinar
				return VirtualEventWebinar.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventPresenter":
				from .virtual_event_presenter import VirtualEventPresenter
				return VirtualEventPresenter.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventRegistration":
				from .virtual_event_registration import VirtualEventRegistration
				return VirtualEventRegistration.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventRegistrationConfiguration":
				from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration
				return VirtualEventRegistrationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventWebinarRegistrationConfiguration":
				from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration
				return VirtualEventWebinarRegistrationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventRegistrationQuestionBase":
				from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase
				return VirtualEventRegistrationQuestionBase.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventRegistrationCustomQuestion":
				from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion
				return VirtualEventRegistrationCustomQuestion.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventRegistrationPredefinedQuestion":
				from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion
				return VirtualEventRegistrationPredefinedQuestion.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventsRoot":
				from .virtual_events_root import VirtualEventsRoot
				return VirtualEventsRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualMachineDetails":
				from .virtual_machine_details import VirtualMachineDetails
				return VirtualMachineDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.vppToken":
				from .vpp_token import VppToken
				return VppToken.model_validate(data)
			if mapping_key == "#microsoft.graph.vulnerableManagedDevice":
				from .vulnerable_managed_device import VulnerableManagedDevice
				return VulnerableManagedDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.webPart":
				from .web_part import WebPart
				return WebPart.model_validate(data)
			if mapping_key == "#microsoft.graph.standardWebPart":
				from .standard_web_part import StandardWebPart
				return StandardWebPart.model_validate(data)
			if mapping_key == "#microsoft.graph.textWebPart":
				from .text_web_part import TextWebPart
				return TextWebPart.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAssignedAccessProfile":
				from .windows_assigned_access_profile import WindowsAssignedAccessProfile
				return WindowsAssignedAccessProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAutopilotDeploymentProfile":
				from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
				return WindowsAutopilotDeploymentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.activeDirectoryWindowsAutopilotDeploymentProfile":
				from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile
				return ActiveDirectoryWindowsAutopilotDeploymentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.azureADWindowsAutopilotDeploymentProfile":
				from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile
				return AzureADWindowsAutopilotDeploymentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAutopilotDeploymentProfileAssignment":
				from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
				return WindowsAutopilotDeploymentProfileAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAutopilotDeviceIdentity":
				from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
				return WindowsAutopilotDeviceIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAutopilotSettings":
				from .windows_autopilot_settings import WindowsAutopilotSettings
				return WindowsAutopilotSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDefenderApplicationControlSupplementalPolicy":
				from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
				return WindowsDefenderApplicationControlSupplementalPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDefenderApplicationControlSupplementalPolicyAssignment":
				from .windows_defender_application_control_supplemental_policy_assignment import WindowsDefenderApplicationControlSupplementalPolicyAssignment
				return WindowsDefenderApplicationControlSupplementalPolicyAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDefenderApplicationControlSupplementalPolicyDeploymentStatus":
				from .windows_defender_application_control_supplemental_policy_deployment_status import WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus
				return WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDefenderApplicationControlSupplementalPolicyDeploymentSummary":
				from .windows_defender_application_control_supplemental_policy_deployment_summary import WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary
				return WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDeviceMalwareState":
				from .windows_device_malware_state import WindowsDeviceMalwareState
				return WindowsDeviceMalwareState.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDriverUpdateInventory":
				from .windows_driver_update_inventory import WindowsDriverUpdateInventory
				return WindowsDriverUpdateInventory.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDriverUpdateProfile":
				from .windows_driver_update_profile import WindowsDriverUpdateProfile
				return WindowsDriverUpdateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDriverUpdateProfileAssignment":
				from .windows_driver_update_profile_assignment import WindowsDriverUpdateProfileAssignment
				return WindowsDriverUpdateProfileAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsFeatureUpdateProfile":
				from .windows_feature_update_profile import WindowsFeatureUpdateProfile
				return WindowsFeatureUpdateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsFeatureUpdateProfileAssignment":
				from .windows_feature_update_profile_assignment import WindowsFeatureUpdateProfileAssignment
				return WindowsFeatureUpdateProfileAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtectionAppLearningSummary":
				from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
				return WindowsInformationProtectionAppLearningSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtectionAppLockerFile":
				from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
				return WindowsInformationProtectionAppLockerFile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtectionDeviceRegistration":
				from .windows_information_protection_device_registration import WindowsInformationProtectionDeviceRegistration
				return WindowsInformationProtectionDeviceRegistration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtectionNetworkLearningSummary":
				from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
				return WindowsInformationProtectionNetworkLearningSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtectionWipeAction":
				from .windows_information_protection_wipe_action import WindowsInformationProtectionWipeAction
				return WindowsInformationProtectionWipeAction.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsMalwareInformation":
				from .windows_malware_information import WindowsMalwareInformation
				return WindowsMalwareInformation.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsManagementApp":
				from .windows_management_app import WindowsManagementApp
				return WindowsManagementApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsManagementAppHealthState":
				from .windows_management_app_health_state import WindowsManagementAppHealthState
				return WindowsManagementAppHealthState.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsManagementAppHealthSummary":
				from .windows_management_app_health_summary import WindowsManagementAppHealthSummary
				return WindowsManagementAppHealthSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPrivacyDataAccessControlItem":
				from .windows_privacy_data_access_control_item import WindowsPrivacyDataAccessControlItem
				return WindowsPrivacyDataAccessControlItem.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsProtectionState":
				from .windows_protection_state import WindowsProtectionState
				return WindowsProtectionState.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsQualityUpdatePolicy":
				from .windows_quality_update_policy import WindowsQualityUpdatePolicy
				return WindowsQualityUpdatePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsQualityUpdatePolicyAssignment":
				from .windows_quality_update_policy_assignment import WindowsQualityUpdatePolicyAssignment
				return WindowsQualityUpdatePolicyAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsQualityUpdateProfile":
				from .windows_quality_update_profile import WindowsQualityUpdateProfile
				return WindowsQualityUpdateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsQualityUpdateProfileAssignment":
				from .windows_quality_update_profile_assignment import WindowsQualityUpdateProfileAssignment
				return WindowsQualityUpdateProfileAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsSetting":
				from .windows_setting import WindowsSetting
				return WindowsSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsSettingInstance":
				from .windows_setting_instance import WindowsSettingInstance
				return WindowsSettingInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdateCatalogItem":
				from .windows_update_catalog_item import WindowsUpdateCatalogItem
				return WindowsUpdateCatalogItem.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsFeatureUpdateCatalogItem":
				from .windows_feature_update_catalog_item import WindowsFeatureUpdateCatalogItem
				return WindowsFeatureUpdateCatalogItem.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsQualityUpdateCatalogItem":
				from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem
				return WindowsQualityUpdateCatalogItem.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdateState":
				from .windows_update_state import WindowsUpdateState
				return WindowsUpdateState.model_validate(data)
			if mapping_key == "#microsoft.graph.workbook":
				from .workbook import Workbook
				return Workbook.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookApplication":
				from .workbook_application import WorkbookApplication
				return WorkbookApplication.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChart":
				from .workbook_chart import WorkbookChart
				return WorkbookChart.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartAreaFormat":
				from .workbook_chart_area_format import WorkbookChartAreaFormat
				return WorkbookChartAreaFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartAxes":
				from .workbook_chart_axes import WorkbookChartAxes
				return WorkbookChartAxes.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartAxis":
				from .workbook_chart_axis import WorkbookChartAxis
				return WorkbookChartAxis.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartAxisFormat":
				from .workbook_chart_axis_format import WorkbookChartAxisFormat
				return WorkbookChartAxisFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartAxisTitle":
				from .workbook_chart_axis_title import WorkbookChartAxisTitle
				return WorkbookChartAxisTitle.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartAxisTitleFormat":
				from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat
				return WorkbookChartAxisTitleFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartDataLabelFormat":
				from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat
				return WorkbookChartDataLabelFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartDataLabels":
				from .workbook_chart_data_labels import WorkbookChartDataLabels
				return WorkbookChartDataLabels.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartFill":
				from .workbook_chart_fill import WorkbookChartFill
				return WorkbookChartFill.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartFont":
				from .workbook_chart_font import WorkbookChartFont
				return WorkbookChartFont.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartGridlines":
				from .workbook_chart_gridlines import WorkbookChartGridlines
				return WorkbookChartGridlines.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartGridlinesFormat":
				from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat
				return WorkbookChartGridlinesFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartLegend":
				from .workbook_chart_legend import WorkbookChartLegend
				return WorkbookChartLegend.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartLegendFormat":
				from .workbook_chart_legend_format import WorkbookChartLegendFormat
				return WorkbookChartLegendFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartLineFormat":
				from .workbook_chart_line_format import WorkbookChartLineFormat
				return WorkbookChartLineFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartPoint":
				from .workbook_chart_point import WorkbookChartPoint
				return WorkbookChartPoint.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartPointFormat":
				from .workbook_chart_point_format import WorkbookChartPointFormat
				return WorkbookChartPointFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartSeries":
				from .workbook_chart_series import WorkbookChartSeries
				return WorkbookChartSeries.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartSeriesFormat":
				from .workbook_chart_series_format import WorkbookChartSeriesFormat
				return WorkbookChartSeriesFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartTitle":
				from .workbook_chart_title import WorkbookChartTitle
				return WorkbookChartTitle.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookChartTitleFormat":
				from .workbook_chart_title_format import WorkbookChartTitleFormat
				return WorkbookChartTitleFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookComment":
				from .workbook_comment import WorkbookComment
				return WorkbookComment.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookCommentReply":
				from .workbook_comment_reply import WorkbookCommentReply
				return WorkbookCommentReply.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookDocumentTask":
				from .workbook_document_task import WorkbookDocumentTask
				return WorkbookDocumentTask.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookDocumentTaskChange":
				from .workbook_document_task_change import WorkbookDocumentTaskChange
				return WorkbookDocumentTaskChange.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookFilter":
				from .workbook_filter import WorkbookFilter
				return WorkbookFilter.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookFormatProtection":
				from .workbook_format_protection import WorkbookFormatProtection
				return WorkbookFormatProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookFunctionResult":
				from .workbook_function_result import WorkbookFunctionResult
				return WorkbookFunctionResult.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookFunctions":
				from .workbook_functions import WorkbookFunctions
				return WorkbookFunctions.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookNamedItem":
				from .workbook_named_item import WorkbookNamedItem
				return WorkbookNamedItem.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookOperation":
				from .workbook_operation import WorkbookOperation
				return WorkbookOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookPivotTable":
				from .workbook_pivot_table import WorkbookPivotTable
				return WorkbookPivotTable.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookRange":
				from .workbook_range import WorkbookRange
				return WorkbookRange.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookRangeBorder":
				from .workbook_range_border import WorkbookRangeBorder
				return WorkbookRangeBorder.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookRangeFill":
				from .workbook_range_fill import WorkbookRangeFill
				return WorkbookRangeFill.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookRangeFont":
				from .workbook_range_font import WorkbookRangeFont
				return WorkbookRangeFont.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookRangeFormat":
				from .workbook_range_format import WorkbookRangeFormat
				return WorkbookRangeFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookRangeSort":
				from .workbook_range_sort import WorkbookRangeSort
				return WorkbookRangeSort.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookRangeView":
				from .workbook_range_view import WorkbookRangeView
				return WorkbookRangeView.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookTable":
				from .workbook_table import WorkbookTable
				return WorkbookTable.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookTableColumn":
				from .workbook_table_column import WorkbookTableColumn
				return WorkbookTableColumn.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookTableRow":
				from .workbook_table_row import WorkbookTableRow
				return WorkbookTableRow.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookTableSort":
				from .workbook_table_sort import WorkbookTableSort
				return WorkbookTableSort.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookWorksheet":
				from .workbook_worksheet import WorkbookWorksheet
				return WorkbookWorksheet.model_validate(data)
			if mapping_key == "#microsoft.graph.workbookWorksheetProtection":
				from .workbook_worksheet_protection import WorkbookWorksheetProtection
				return WorkbookWorksheetProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.workingTimeSchedule":
				from .working_time_schedule import WorkingTimeSchedule
				return WorkingTimeSchedule.model_validate(data)
			if mapping_key == "#microsoft.graph.workplaceSensorDevice":
				from .workplace_sensor_device import WorkplaceSensorDevice
				return WorkplaceSensorDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.zebraFotaArtifact":
				from .zebra_fota_artifact import ZebraFotaArtifact
				return ZebraFotaArtifact.model_validate(data)
			if mapping_key == "#microsoft.graph.zebraFotaConnector":
				from .zebra_fota_connector import ZebraFotaConnector
				return ZebraFotaConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.zebraFotaDeployment":
				from .zebra_fota_deployment import ZebraFotaDeployment
				return ZebraFotaDeployment.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecords.callRecord":
				from .call_records_call_record import CallRecordsCallRecord
				return CallRecordsCallRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecords.participantBase":
				from .call_records_participant_base import CallRecordsParticipantBase
				return CallRecordsParticipantBase.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecords.organizer":
				from .call_records_organizer import CallRecordsOrganizer
				return CallRecordsOrganizer.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecords.participant":
				from .call_records_participant import CallRecordsParticipant
				return CallRecordsParticipant.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecords.segment":
				from .call_records_segment import CallRecordsSegment
				return CallRecordsSegment.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecords.session":
				from .call_records_session import CallRecordsSession
				return CallRecordsSession.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudLicensing.usageRight":
				from .cloud_licensing_usage_right import CloudLicensingUsageRight
				return CloudLicensingUsageRight.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagement.alertRecord":
				from .device_management_alert_record import DeviceManagementAlertRecord
				return DeviceManagementAlertRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagement.alertRule":
				from .device_management_alert_rule import DeviceManagementAlertRule
				return DeviceManagementAlertRule.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagement.monitoring":
				from .device_management_monitoring import DeviceManagementMonitoring
				return DeviceManagementMonitoring.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.case":
				from .ediscovery_case import EdiscoveryCase
				return EdiscoveryCase.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.caseOperation":
				from .ediscovery_case_operation import EdiscoveryCaseOperation
				return EdiscoveryCaseOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.addToReviewSetOperation":
				from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
				return EdiscoveryAddToReviewSetOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.caseExportOperation":
				from .ediscovery_case_export_operation import EdiscoveryCaseExportOperation
				return EdiscoveryCaseExportOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.caseHoldOperation":
				from .ediscovery_case_hold_operation import EdiscoveryCaseHoldOperation
				return EdiscoveryCaseHoldOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.caseIndexOperation":
				from .ediscovery_case_index_operation import EdiscoveryCaseIndexOperation
				return EdiscoveryCaseIndexOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.estimateStatisticsOperation":
				from .ediscovery_estimate_statistics_operation import EdiscoveryEstimateStatisticsOperation
				return EdiscoveryEstimateStatisticsOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.purgeDataOperation":
				from .ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
				return EdiscoveryPurgeDataOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.tagOperation":
				from .ediscovery_tag_operation import EdiscoveryTagOperation
				return EdiscoveryTagOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.caseSettings":
				from .ediscovery_case_settings import EdiscoveryCaseSettings
				return EdiscoveryCaseSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.dataSource":
				from .ediscovery_data_source import EdiscoveryDataSource
				return EdiscoveryDataSource.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.siteSource":
				from .ediscovery_site_source import EdiscoverySiteSource
				return EdiscoverySiteSource.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.unifiedGroupSource":
				from .ediscovery_unified_group_source import EdiscoveryUnifiedGroupSource
				return EdiscoveryUnifiedGroupSource.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.userSource":
				from .ediscovery_user_source import EdiscoveryUserSource
				return EdiscoveryUserSource.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.dataSourceContainer":
				from .ediscovery_data_source_container import EdiscoveryDataSourceContainer
				return EdiscoveryDataSourceContainer.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.custodian":
				from .ediscovery_custodian import EdiscoveryCustodian
				return EdiscoveryCustodian.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.noncustodialDataSource":
				from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
				return EdiscoveryNoncustodialDataSource.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.ediscoveryroot":
				from .ediscovery_ediscoveryroot import EdiscoveryEdiscoveryroot
				return EdiscoveryEdiscoveryroot.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.legalHold":
				from .ediscovery_legal_hold import EdiscoveryLegalHold
				return EdiscoveryLegalHold.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.reviewSet":
				from .ediscovery_review_set import EdiscoveryReviewSet
				return EdiscoveryReviewSet.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.reviewSetQuery":
				from .ediscovery_review_set_query import EdiscoveryReviewSetQuery
				return EdiscoveryReviewSetQuery.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.sourceCollection":
				from .ediscovery_source_collection import EdiscoverySourceCollection
				return EdiscoverySourceCollection.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.tag":
				from .ediscovery_tag import EdiscoveryTag
				return EdiscoveryTag.model_validate(data)
			if mapping_key == "#microsoft.graph.externalConnectors.connectionOperation":
				from .external_connectors_connection_operation import ExternalConnectorsConnectionOperation
				return ExternalConnectorsConnectionOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.externalConnectors.connectionQuota":
				from .external_connectors_connection_quota import ExternalConnectorsConnectionQuota
				return ExternalConnectorsConnectionQuota.model_validate(data)
			if mapping_key == "#microsoft.graph.externalConnectors.externalActivity":
				from .external_connectors_external_activity import ExternalConnectorsExternalActivity
				return ExternalConnectorsExternalActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.externalConnectors.externalActivityResult":
				from .external_connectors_external_activity_result import ExternalConnectorsExternalActivityResult
				return ExternalConnectorsExternalActivityResult.model_validate(data)
			if mapping_key == "#microsoft.graph.externalConnectors.externalConnection":
				from .external_connectors_external_connection import ExternalConnectorsExternalConnection
				return ExternalConnectorsExternalConnection.model_validate(data)
			if mapping_key == "#microsoft.graph.externalConnectors.externalGroup":
				from .external_connectors_external_group import ExternalConnectorsExternalGroup
				return ExternalConnectorsExternalGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.externalConnectors.externalItem":
				from .external_connectors_external_item import ExternalConnectorsExternalItem
				return ExternalConnectorsExternalItem.model_validate(data)
			if mapping_key == "#microsoft.graph.externalConnectors.identity":
				from .external_connectors_identity import ExternalConnectorsIdentity
				return ExternalConnectorsIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.externalConnectors.schema":
				from .external_connectors_schema import ExternalConnectorsSchema
				return ExternalConnectorsSchema.model_validate(data)
			if mapping_key == "#microsoft.graph.healthMonitoring.alert":
				from .health_monitoring_alert import HealthMonitoringAlert
				return HealthMonitoringAlert.model_validate(data)
			if mapping_key == "#microsoft.graph.healthMonitoring.alertConfiguration":
				from .health_monitoring_alert_configuration import HealthMonitoringAlertConfiguration
				return HealthMonitoringAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.healthMonitoring.healthMonitoringRoot":
				from .health_monitoring_health_monitoring_root import HealthMonitoringHealthMonitoringRoot
				return HealthMonitoringHealthMonitoringRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.insights":
				from .identity_governance_insights import IdentityGovernanceInsights
				return IdentityGovernanceInsights.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.lifecycleManagementSettings":
				from .identity_governance_lifecycle_management_settings import IdentityGovernanceLifecycleManagementSettings
				return IdentityGovernanceLifecycleManagementSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.lifecycleWorkflowsContainer":
				from .identity_governance_lifecycle_workflows_container import IdentityGovernanceLifecycleWorkflowsContainer
				return IdentityGovernanceLifecycleWorkflowsContainer.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.run":
				from .identity_governance_run import IdentityGovernanceRun
				return IdentityGovernanceRun.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.task":
				from .identity_governance_task import IdentityGovernanceTask
				return IdentityGovernanceTask.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.taskDefinition":
				from .identity_governance_task_definition import IdentityGovernanceTaskDefinition
				return IdentityGovernanceTaskDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.taskProcessingResult":
				from .identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult
				return IdentityGovernanceTaskProcessingResult.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.taskReport":
				from .identity_governance_task_report import IdentityGovernanceTaskReport
				return IdentityGovernanceTaskReport.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.userProcessingResult":
				from .identity_governance_user_processing_result import IdentityGovernanceUserProcessingResult
				return IdentityGovernanceUserProcessingResult.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.workflowTemplate":
				from .identity_governance_workflow_template import IdentityGovernanceWorkflowTemplate
				return IdentityGovernanceWorkflowTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.industryDataActivity":
				from .industry_data_industry_data_activity import IndustryDataIndustryDataActivity
				return IndustryDataIndustryDataActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.inboundFlow":
				from .industry_data_inbound_flow import IndustryDataInboundFlow
				return IndustryDataInboundFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.inboundApiFlow":
				from .industry_data_inbound_api_flow import IndustryDataInboundApiFlow
				return IndustryDataInboundApiFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.inboundFileFlow":
				from .industry_data_inbound_file_flow import IndustryDataInboundFileFlow
				return IndustryDataInboundFileFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.industryDataConnector":
				from .industry_data_industry_data_connector import IndustryDataIndustryDataConnector
				return IndustryDataIndustryDataConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.apiDataConnector":
				from .industry_data_api_data_connector import IndustryDataApiDataConnector
				return IndustryDataApiDataConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.oneRosterApiDataConnector":
				from .industry_data_one_roster_api_data_connector import IndustryDataOneRosterApiDataConnector
				return IndustryDataOneRosterApiDataConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.fileDataConnector":
				from .industry_data_file_data_connector import IndustryDataFileDataConnector
				return IndustryDataFileDataConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.azureDataLakeConnector":
				from .industry_data_azure_data_lake_connector import IndustryDataAzureDataLakeConnector
				return IndustryDataAzureDataLakeConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.industryDataRoot":
				from .industry_data_industry_data_root import IndustryDataIndustryDataRoot
				return IndustryDataIndustryDataRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.industryDataRun":
				from .industry_data_industry_data_run import IndustryDataIndustryDataRun
				return IndustryDataIndustryDataRun.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.industryDataRunActivity":
				from .industry_data_industry_data_run_activity import IndustryDataIndustryDataRunActivity
				return IndustryDataIndustryDataRunActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.inboundFlowActivity":
				from .industry_data_inbound_flow_activity import IndustryDataInboundFlowActivity
				return IndustryDataInboundFlowActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.outboundFlowActivity":
				from .industry_data_outbound_flow_activity import IndustryDataOutboundFlowActivity
				return IndustryDataOutboundFlowActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.outboundProvisioningFlowSet":
				from .industry_data_outbound_provisioning_flow_set import IndustryDataOutboundProvisioningFlowSet
				return IndustryDataOutboundProvisioningFlowSet.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.provisioningFlow":
				from .industry_data_provisioning_flow import IndustryDataProvisioningFlow
				return IndustryDataProvisioningFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.administrativeUnitProvisioningFlow":
				from .industry_data_administrative_unit_provisioning_flow import IndustryDataAdministrativeUnitProvisioningFlow
				return IndustryDataAdministrativeUnitProvisioningFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.classGroupProvisioningFlow":
				from .industry_data_class_group_provisioning_flow import IndustryDataClassGroupProvisioningFlow
				return IndustryDataClassGroupProvisioningFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.securityGroupProvisioningFlow":
				from .industry_data_security_group_provisioning_flow import IndustryDataSecurityGroupProvisioningFlow
				return IndustryDataSecurityGroupProvisioningFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.userProvisioningFlow":
				from .industry_data_user_provisioning_flow import IndustryDataUserProvisioningFlow
				return IndustryDataUserProvisioningFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.referenceDefinition":
				from .industry_data_reference_definition import IndustryDataReferenceDefinition
				return IndustryDataReferenceDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.roleGroup":
				from .industry_data_role_group import IndustryDataRoleGroup
				return IndustryDataRoleGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.sourceSystemDefinition":
				from .industry_data_source_system_definition import IndustryDataSourceSystemDefinition
				return IndustryDataSourceSystemDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.yearTimePeriodDefinition":
				from .industry_data_year_time_period_definition import IndustryDataYearTimePeriodDefinition
				return IndustryDataYearTimePeriodDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.aggregatedPolicyCompliance":
				from .managed_tenants_aggregated_policy_compliance import ManagedTenantsAggregatedPolicyCompliance
				return ManagedTenantsAggregatedPolicyCompliance.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.appPerformance":
				from .managed_tenants_app_performance import ManagedTenantsAppPerformance
				return ManagedTenantsAppPerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.auditEvent":
				from .managed_tenants_audit_event import ManagedTenantsAuditEvent
				return ManagedTenantsAuditEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.cloudPcConnection":
				from .managed_tenants_cloud_pc_connection import ManagedTenantsCloudPcConnection
				return ManagedTenantsCloudPcConnection.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.cloudPcDevice":
				from .managed_tenants_cloud_pc_device import ManagedTenantsCloudPcDevice
				return ManagedTenantsCloudPcDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.cloudPcOverview":
				from .managed_tenants_cloud_pc_overview import ManagedTenantsCloudPcOverview
				return ManagedTenantsCloudPcOverview.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.conditionalAccessPolicyCoverage":
				from .managed_tenants_conditional_access_policy_coverage import ManagedTenantsConditionalAccessPolicyCoverage
				return ManagedTenantsConditionalAccessPolicyCoverage.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.credentialUserRegistrationsSummary":
				from .managed_tenants_credential_user_registrations_summary import ManagedTenantsCredentialUserRegistrationsSummary
				return ManagedTenantsCredentialUserRegistrationsSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.deviceAppPerformance":
				from .managed_tenants_device_app_performance import ManagedTenantsDeviceAppPerformance
				return ManagedTenantsDeviceAppPerformance.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.deviceCompliancePolicySettingStateSummary":
				from .managed_tenants_device_compliance_policy_setting_state_summary import ManagedTenantsDeviceCompliancePolicySettingStateSummary
				return ManagedTenantsDeviceCompliancePolicySettingStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.deviceHealthStatus":
				from .managed_tenants_device_health_status import ManagedTenantsDeviceHealthStatus
				return ManagedTenantsDeviceHealthStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managedDeviceCompliance":
				from .managed_tenants_managed_device_compliance import ManagedTenantsManagedDeviceCompliance
				return ManagedTenantsManagedDeviceCompliance.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managedDeviceComplianceTrend":
				from .managed_tenants_managed_device_compliance_trend import ManagedTenantsManagedDeviceComplianceTrend
				return ManagedTenantsManagedDeviceComplianceTrend.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managedTenant":
				from .managed_tenants_managed_tenant import ManagedTenantsManagedTenant
				return ManagedTenantsManagedTenant.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managedTenantAlert":
				from .managed_tenants_managed_tenant_alert import ManagedTenantsManagedTenantAlert
				return ManagedTenantsManagedTenantAlert.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managedTenantAlertLog":
				from .managed_tenants_managed_tenant_alert_log import ManagedTenantsManagedTenantAlertLog
				return ManagedTenantsManagedTenantAlertLog.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managedTenantAlertRule":
				from .managed_tenants_managed_tenant_alert_rule import ManagedTenantsManagedTenantAlertRule
				return ManagedTenantsManagedTenantAlertRule.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managedTenantAlertRuleDefinition":
				from .managed_tenants_managed_tenant_alert_rule_definition import ManagedTenantsManagedTenantAlertRuleDefinition
				return ManagedTenantsManagedTenantAlertRuleDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managedTenantApiNotification":
				from .managed_tenants_managed_tenant_api_notification import ManagedTenantsManagedTenantApiNotification
				return ManagedTenantsManagedTenantApiNotification.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managedTenantEmailNotification":
				from .managed_tenants_managed_tenant_email_notification import ManagedTenantsManagedTenantEmailNotification
				return ManagedTenantsManagedTenantEmailNotification.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managedTenantTicketingEndpoint":
				from .managed_tenants_managed_tenant_ticketing_endpoint import ManagedTenantsManagedTenantTicketingEndpoint
				return ManagedTenantsManagedTenantTicketingEndpoint.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managementAction":
				from .managed_tenants_management_action import ManagedTenantsManagementAction
				return ManagedTenantsManagementAction.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managementActionTenantDeploymentStatus":
				from .managed_tenants_management_action_tenant_deployment_status import ManagedTenantsManagementActionTenantDeploymentStatus
				return ManagedTenantsManagementActionTenantDeploymentStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managementIntent":
				from .managed_tenants_management_intent import ManagedTenantsManagementIntent
				return ManagedTenantsManagementIntent.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managementTemplate":
				from .managed_tenants_management_template import ManagedTenantsManagementTemplate
				return ManagedTenantsManagementTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managementTemplateCollection":
				from .managed_tenants_management_template_collection import ManagedTenantsManagementTemplateCollection
				return ManagedTenantsManagementTemplateCollection.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managementTemplateCollectionTenantSummary":
				from .managed_tenants_management_template_collection_tenant_summary import ManagedTenantsManagementTemplateCollectionTenantSummary
				return ManagedTenantsManagementTemplateCollectionTenantSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managementTemplateStep":
				from .managed_tenants_management_template_step import ManagedTenantsManagementTemplateStep
				return ManagedTenantsManagementTemplateStep.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managementTemplateStepDeployment":
				from .managed_tenants_management_template_step_deployment import ManagedTenantsManagementTemplateStepDeployment
				return ManagedTenantsManagementTemplateStepDeployment.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managementTemplateStepTenantSummary":
				from .managed_tenants_management_template_step_tenant_summary import ManagedTenantsManagementTemplateStepTenantSummary
				return ManagedTenantsManagementTemplateStepTenantSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managementTemplateStepVersion":
				from .managed_tenants_management_template_step_version import ManagedTenantsManagementTemplateStepVersion
				return ManagedTenantsManagementTemplateStepVersion.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.tenant":
				from .managed_tenants_tenant import ManagedTenantsTenant
				return ManagedTenantsTenant.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.tenantCustomizedInformation":
				from .managed_tenants_tenant_customized_information import ManagedTenantsTenantCustomizedInformation
				return ManagedTenantsTenantCustomizedInformation.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.tenantDetailedInformation":
				from .managed_tenants_tenant_detailed_information import ManagedTenantsTenantDetailedInformation
				return ManagedTenantsTenantDetailedInformation.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.tenantGroup":
				from .managed_tenants_tenant_group import ManagedTenantsTenantGroup
				return ManagedTenantsTenantGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.tenantTag":
				from .managed_tenants_tenant_tag import ManagedTenantsTenantTag
				return ManagedTenantsTenantTag.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.windowsDeviceMalwareState":
				from .managed_tenants_windows_device_malware_state import ManagedTenantsWindowsDeviceMalwareState
				return ManagedTenantsWindowsDeviceMalwareState.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.windowsProtectionState":
				from .managed_tenants_windows_protection_state import ManagedTenantsWindowsProtectionState
				return ManagedTenantsWindowsProtectionState.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.alert":
				from .networkaccess_alert import NetworkaccessAlert
				return NetworkaccessAlert.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.branchSite":
				from .networkaccess_branch_site import NetworkaccessBranchSite
				return NetworkaccessBranchSite.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.conditionalAccessPolicy":
				from .networkaccess_conditional_access_policy import NetworkaccessConditionalAccessPolicy
				return NetworkaccessConditionalAccessPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.conditionalAccessSettings":
				from .networkaccess_conditional_access_settings import NetworkaccessConditionalAccessSettings
				return NetworkaccessConditionalAccessSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.connectivity":
				from .networkaccess_connectivity import NetworkaccessConnectivity
				return NetworkaccessConnectivity.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.connectivityConfigurationLink":
				from .networkaccess_connectivity_configuration_link import NetworkaccessConnectivityConfigurationLink
				return NetworkaccessConnectivityConfigurationLink.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.crossTenantAccessSettings":
				from .networkaccess_cross_tenant_access_settings import NetworkaccessCrossTenantAccessSettings
				return NetworkaccessCrossTenantAccessSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.deviceLink":
				from .networkaccess_device_link import NetworkaccessDeviceLink
				return NetworkaccessDeviceLink.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.enrichedAuditLogs":
				from .networkaccess_enriched_audit_logs import NetworkaccessEnrichedAuditLogs
				return NetworkaccessEnrichedAuditLogs.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.forwardingOptions":
				from .networkaccess_forwarding_options import NetworkaccessForwardingOptions
				return NetworkaccessForwardingOptions.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.logs":
				from .networkaccess_logs import NetworkaccessLogs
				return NetworkaccessLogs.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.networkAccessRoot":
				from .networkaccess_network_access_root import NetworkaccessNetworkAccessRoot
				return NetworkaccessNetworkAccessRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.policy":
				from .networkaccess_policy import NetworkaccessPolicy
				return NetworkaccessPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.filteringPolicy":
				from .networkaccess_filtering_policy import NetworkaccessFilteringPolicy
				return NetworkaccessFilteringPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.forwardingPolicy":
				from .networkaccess_forwarding_policy import NetworkaccessForwardingPolicy
				return NetworkaccessForwardingPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.policyLink":
				from .networkaccess_policy_link import NetworkaccessPolicyLink
				return NetworkaccessPolicyLink.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.filteringPolicyLink":
				from .networkaccess_filtering_policy_link import NetworkaccessFilteringPolicyLink
				return NetworkaccessFilteringPolicyLink.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.forwardingPolicyLink":
				from .networkaccess_forwarding_policy_link import NetworkaccessForwardingPolicyLink
				return NetworkaccessForwardingPolicyLink.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.policyRule":
				from .networkaccess_policy_rule import NetworkaccessPolicyRule
				return NetworkaccessPolicyRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.filteringRule":
				from .networkaccess_filtering_rule import NetworkaccessFilteringRule
				return NetworkaccessFilteringRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.fqdnFilteringRule":
				from .networkaccess_fqdn_filtering_rule import NetworkaccessFqdnFilteringRule
				return NetworkaccessFqdnFilteringRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.webCategoryFilteringRule":
				from .networkaccess_web_category_filtering_rule import NetworkaccessWebCategoryFilteringRule
				return NetworkaccessWebCategoryFilteringRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.forwardingRule":
				from .networkaccess_forwarding_rule import NetworkaccessForwardingRule
				return NetworkaccessForwardingRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.internetAccessForwardingRule":
				from .networkaccess_internet_access_forwarding_rule import NetworkaccessInternetAccessForwardingRule
				return NetworkaccessInternetAccessForwardingRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.m365ForwardingRule":
				from .networkaccess_m365_forwarding_rule import NetworkaccessM365ForwardingRule
				return NetworkaccessM365ForwardingRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.privateAccessForwardingRule":
				from .networkaccess_private_access_forwarding_rule import NetworkaccessPrivateAccessForwardingRule
				return NetworkaccessPrivateAccessForwardingRule.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.profile":
				from .networkaccess_profile import NetworkaccessProfile
				return NetworkaccessProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.filteringProfile":
				from .networkaccess_filtering_profile import NetworkaccessFilteringProfile
				return NetworkaccessFilteringProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.forwardingProfile":
				from .networkaccess_forwarding_profile import NetworkaccessForwardingProfile
				return NetworkaccessForwardingProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.remoteNetwork":
				from .networkaccess_remote_network import NetworkaccessRemoteNetwork
				return NetworkaccessRemoteNetwork.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.remoteNetworkHealthEvent":
				from .networkaccess_remote_network_health_event import NetworkaccessRemoteNetworkHealthEvent
				return NetworkaccessRemoteNetworkHealthEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.reports":
				from .networkaccess_reports import NetworkaccessReports
				return NetworkaccessReports.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.settings":
				from .networkaccess_settings import NetworkaccessSettings
				return NetworkaccessSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.tenantStatus":
				from .networkaccess_tenant_status import NetworkaccessTenantStatus
				return NetworkaccessTenantStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.partnerSecurity":
				from .partner_security_partner_security import PartnerSecurityPartnerSecurity
				return PartnerSecurityPartnerSecurity.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.partnerSecurityAlert":
				from .partner_security_partner_security_alert import PartnerSecurityPartnerSecurityAlert
				return PartnerSecurityPartnerSecurityAlert.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.partnerSecurityScore":
				from .partner_security_partner_security_score import PartnerSecurityPartnerSecurityScore
				return PartnerSecurityPartnerSecurityScore.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.securityRequirement":
				from .partner_security_security_requirement import PartnerSecuritySecurityRequirement
				return PartnerSecuritySecurityRequirement.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.adminsMfaEnforcedSecurityRequirement":
				from .partner_security_admins_mfa_enforced_security_requirement import PartnerSecurityAdminsMfaEnforcedSecurityRequirement
				return PartnerSecurityAdminsMfaEnforcedSecurityRequirement.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.customersMfaEnforcedSecurityRequirement":
				from .partner_security_customers_mfa_enforced_security_requirement import PartnerSecurityCustomersMfaEnforcedSecurityRequirement
				return PartnerSecurityCustomersMfaEnforcedSecurityRequirement.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.customersSpendingBudgetSecurityRequirement":
				from .partner_security_customers_spending_budget_security_requirement import PartnerSecurityCustomersSpendingBudgetSecurityRequirement
				return PartnerSecurityCustomersSpendingBudgetSecurityRequirement.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.responseTimeSecurityRequirement":
				from .partner_security_response_time_security_requirement import PartnerSecurityResponseTimeSecurityRequirement
				return PartnerSecurityResponseTimeSecurityRequirement.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.securityScoreHistory":
				from .partner_security_security_score_history import PartnerSecuritySecurityScoreHistory
				return PartnerSecuritySecurityScoreHistory.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.azureUsage":
				from .partners_billing_azure_usage import PartnersBillingAzureUsage
				return PartnersBillingAzureUsage.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.billedReconciliation":
				from .partners_billing_billed_reconciliation import PartnersBillingBilledReconciliation
				return PartnersBillingBilledReconciliation.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.billedUsage":
				from .partners_billing_billed_usage import PartnersBillingBilledUsage
				return PartnersBillingBilledUsage.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.billing":
				from .partners_billing_billing import PartnersBillingBilling
				return PartnersBillingBilling.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.billingReconciliation":
				from .partners_billing_billing_reconciliation import PartnersBillingBillingReconciliation
				return PartnersBillingBillingReconciliation.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.manifest":
				from .partners_billing_manifest import PartnersBillingManifest
				return PartnersBillingManifest.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.operation":
				from .partners_billing_operation import PartnersBillingOperation
				return PartnersBillingOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.exportSuccessOperation":
				from .partners_billing_export_success_operation import PartnersBillingExportSuccessOperation
				return PartnersBillingExportSuccessOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.failedOperation":
				from .partners_billing_failed_operation import PartnersBillingFailedOperation
				return PartnersBillingFailedOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.runningOperation":
				from .partners_billing_running_operation import PartnersBillingRunningOperation
				return PartnersBillingRunningOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.unbilledUsage":
				from .partners_billing_unbilled_usage import PartnersBillingUnbilledUsage
				return PartnersBillingUnbilledUsage.model_validate(data)
			if mapping_key == "#microsoft.graph.search.searchAnswer":
				from .search_search_answer import SearchSearchAnswer
				return SearchSearchAnswer.model_validate(data)
			if mapping_key == "#microsoft.graph.search.acronym":
				from .search_acronym import SearchAcronym
				return SearchAcronym.model_validate(data)
			if mapping_key == "#microsoft.graph.search.bookmark":
				from .search_bookmark import SearchBookmark
				return SearchBookmark.model_validate(data)
			if mapping_key == "#microsoft.graph.search.qna":
				from .search_qna import SearchQna
				return SearchQna.model_validate(data)
			if mapping_key == "#microsoft.graph.security.alert":
				from .security_alert import SecurityAlert
				return SecurityAlert.model_validate(data)
			if mapping_key == "#microsoft.graph.security.analyzedEmail":
				from .security_analyzed_email import SecurityAnalyzedEmail
				return SecurityAnalyzedEmail.model_validate(data)
			if mapping_key == "#microsoft.graph.security.article":
				from .security_article import SecurityArticle
				return SecurityArticle.model_validate(data)
			if mapping_key == "#microsoft.graph.security.artifact":
				from .security_artifact import SecurityArtifact
				return SecurityArtifact.model_validate(data)
			if mapping_key == "#microsoft.graph.security.host":
				from .security_host import SecurityHost
				return SecurityHost.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostname":
				from .security_hostname import SecurityHostname
				return SecurityHostname.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ipAddress":
				from .security_ip_address import SecurityIpAddress
				return SecurityIpAddress.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostComponent":
				from .security_host_component import SecurityHostComponent
				return SecurityHostComponent.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostCookie":
				from .security_host_cookie import SecurityHostCookie
				return SecurityHostCookie.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostSslCertificate":
				from .security_host_ssl_certificate import SecurityHostSslCertificate
				return SecurityHostSslCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostTracker":
				from .security_host_tracker import SecurityHostTracker
				return SecurityHostTracker.model_validate(data)
			if mapping_key == "#microsoft.graph.security.passiveDnsRecord":
				from .security_passive_dns_record import SecurityPassiveDnsRecord
				return SecurityPassiveDnsRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sslCertificate":
				from .security_ssl_certificate import SecuritySslCertificate
				return SecuritySslCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.unclassifiedArtifact":
				from .security_unclassified_artifact import SecurityUnclassifiedArtifact
				return SecurityUnclassifiedArtifact.model_validate(data)
			if mapping_key == "#microsoft.graph.security.auditCoreRoot":
				from .security_audit_core_root import SecurityAuditCoreRoot
				return SecurityAuditCoreRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.security.auditLogQuery":
				from .security_audit_log_query import SecurityAuditLogQuery
				return SecurityAuditLogQuery.model_validate(data)
			if mapping_key == "#microsoft.graph.security.auditLogRecord":
				from .security_audit_log_record import SecurityAuditLogRecord
				return SecurityAuditLogRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.case":
				from .security_case import SecurityCase
				return SecurityCase.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryCase":
				from .security_ediscovery_case import SecurityEdiscoveryCase
				return SecurityEdiscoveryCase.model_validate(data)
			if mapping_key == "#microsoft.graph.security.caseOperation":
				from .security_case_operation import SecurityCaseOperation
				return SecurityCaseOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryAddToReviewSetOperation":
				from .security_ediscovery_add_to_review_set_operation import SecurityEdiscoveryAddToReviewSetOperation
				return SecurityEdiscoveryAddToReviewSetOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryEstimateOperation":
				from .security_ediscovery_estimate_operation import SecurityEdiscoveryEstimateOperation
				return SecurityEdiscoveryEstimateOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryExportOperation":
				from .security_ediscovery_export_operation import SecurityEdiscoveryExportOperation
				return SecurityEdiscoveryExportOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryHoldOperation":
				from .security_ediscovery_hold_operation import SecurityEdiscoveryHoldOperation
				return SecurityEdiscoveryHoldOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryIndexOperation":
				from .security_ediscovery_index_operation import SecurityEdiscoveryIndexOperation
				return SecurityEdiscoveryIndexOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryPurgeDataOperation":
				from .security_ediscovery_purge_data_operation import SecurityEdiscoveryPurgeDataOperation
				return SecurityEdiscoveryPurgeDataOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoverySearchExportOperation":
				from .security_ediscovery_search_export_operation import SecurityEdiscoverySearchExportOperation
				return SecurityEdiscoverySearchExportOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryTagOperation":
				from .security_ediscovery_tag_operation import SecurityEdiscoveryTagOperation
				return SecurityEdiscoveryTagOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.casesRoot":
				from .security_cases_root import SecurityCasesRoot
				return SecurityCasesRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cloudAppDiscoveryReport":
				from .security_cloud_app_discovery_report import SecurityCloudAppDiscoveryReport
				return SecurityCloudAppDiscoveryReport.model_validate(data)
			if mapping_key == "#microsoft.graph.security.collaborationRoot":
				from .security_collaboration_root import SecurityCollaborationRoot
				return SecurityCollaborationRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dataDiscoveryReport":
				from .security_data_discovery_report import SecurityDataDiscoveryReport
				return SecurityDataDiscoveryReport.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dataDiscoveryRoot":
				from .security_data_discovery_root import SecurityDataDiscoveryRoot
				return SecurityDataDiscoveryRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dataSet":
				from .security_data_set import SecurityDataSet
				return SecurityDataSet.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryReviewSet":
				from .security_ediscovery_review_set import SecurityEdiscoveryReviewSet
				return SecurityEdiscoveryReviewSet.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dataSource":
				from .security_data_source import SecurityDataSource
				return SecurityDataSource.model_validate(data)
			if mapping_key == "#microsoft.graph.security.siteSource":
				from .security_site_source import SecuritySiteSource
				return SecuritySiteSource.model_validate(data)
			if mapping_key == "#microsoft.graph.security.unifiedGroupSource":
				from .security_unified_group_source import SecurityUnifiedGroupSource
				return SecurityUnifiedGroupSource.model_validate(data)
			if mapping_key == "#microsoft.graph.security.userSource":
				from .security_user_source import SecurityUserSource
				return SecurityUserSource.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dataSourceContainer":
				from .security_data_source_container import SecurityDataSourceContainer
				return SecurityDataSourceContainer.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryCustodian":
				from .security_ediscovery_custodian import SecurityEdiscoveryCustodian
				return SecurityEdiscoveryCustodian.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryNoncustodialDataSource":
				from .security_ediscovery_noncustodial_data_source import SecurityEdiscoveryNoncustodialDataSource
				return SecurityEdiscoveryNoncustodialDataSource.model_validate(data)
			if mapping_key == "#microsoft.graph.security.discoveredCloudAppDetail":
				from .security_discovered_cloud_app_detail import SecurityDiscoveredCloudAppDetail
				return SecurityDiscoveredCloudAppDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.security.endpointDiscoveredCloudAppDetail":
				from .security_endpoint_discovered_cloud_app_detail import SecurityEndpointDiscoveredCloudAppDetail
				return SecurityEndpointDiscoveredCloudAppDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.security.discoveredCloudAppInfo":
				from .security_discovered_cloud_app_info import SecurityDiscoveredCloudAppInfo
				return SecurityDiscoveredCloudAppInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dispositionReviewStage":
				from .security_disposition_review_stage import SecurityDispositionReviewStage
				return SecurityDispositionReviewStage.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryCaseMember":
				from .security_ediscovery_case_member import SecurityEdiscoveryCaseMember
				return SecurityEdiscoveryCaseMember.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryCaseSettings":
				from .security_ediscovery_case_settings import SecurityEdiscoveryCaseSettings
				return SecurityEdiscoveryCaseSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.security.emailThreatSubmissionPolicy":
				from .security_email_threat_submission_policy import SecurityEmailThreatSubmissionPolicy
				return SecurityEmailThreatSubmissionPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.security.file":
				from .security_file import SecurityFile
				return SecurityFile.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryFile":
				from .security_ediscovery_file import SecurityEdiscoveryFile
				return SecurityEdiscoveryFile.model_validate(data)
			if mapping_key == "#microsoft.graph.security.filePlanDescriptor":
				from .security_file_plan_descriptor import SecurityFilePlanDescriptor
				return SecurityFilePlanDescriptor.model_validate(data)
			if mapping_key == "#microsoft.graph.security.filePlanDescriptorTemplate":
				from .security_file_plan_descriptor_template import SecurityFilePlanDescriptorTemplate
				return SecurityFilePlanDescriptorTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.authorityTemplate":
				from .security_authority_template import SecurityAuthorityTemplate
				return SecurityAuthorityTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.categoryTemplate":
				from .security_category_template import SecurityCategoryTemplate
				return SecurityCategoryTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.citationTemplate":
				from .security_citation_template import SecurityCitationTemplate
				return SecurityCitationTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.departmentTemplate":
				from .security_department_template import SecurityDepartmentTemplate
				return SecurityDepartmentTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.filePlanReferenceTemplate":
				from .security_file_plan_reference_template import SecurityFilePlanReferenceTemplate
				return SecurityFilePlanReferenceTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.subcategoryTemplate":
				from .security_subcategory_template import SecuritySubcategoryTemplate
				return SecuritySubcategoryTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.security.healthIssue":
				from .security_health_issue import SecurityHealthIssue
				return SecurityHealthIssue.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostPair":
				from .security_host_pair import SecurityHostPair
				return SecurityHostPair.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostPort":
				from .security_host_port import SecurityHostPort
				return SecurityHostPort.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostReputation":
				from .security_host_reputation import SecurityHostReputation
				return SecurityHostReputation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.identityContainer":
				from .security_identity_container import SecurityIdentityContainer
				return SecurityIdentityContainer.model_validate(data)
			if mapping_key == "#microsoft.graph.security.incident":
				from .security_incident import SecurityIncident
				return SecurityIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.security.indicator":
				from .security_indicator import SecurityIndicator
				return SecurityIndicator.model_validate(data)
			if mapping_key == "#microsoft.graph.security.articleIndicator":
				from .security_article_indicator import SecurityArticleIndicator
				return SecurityArticleIndicator.model_validate(data)
			if mapping_key == "#microsoft.graph.security.intelligenceProfileIndicator":
				from .security_intelligence_profile_indicator import SecurityIntelligenceProfileIndicator
				return SecurityIntelligenceProfileIndicator.model_validate(data)
			if mapping_key == "#microsoft.graph.security.informationProtection":
				from .security_information_protection import SecurityInformationProtection
				return SecurityInformationProtection.model_validate(data)
			if mapping_key == "#microsoft.graph.security.informationProtectionPolicySetting":
				from .security_information_protection_policy_setting import SecurityInformationProtectionPolicySetting
				return SecurityInformationProtectionPolicySetting.model_validate(data)
			if mapping_key == "#microsoft.graph.security.intelligenceProfile":
				from .security_intelligence_profile import SecurityIntelligenceProfile
				return SecurityIntelligenceProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.security.labelsRoot":
				from .security_labels_root import SecurityLabelsRoot
				return SecurityLabelsRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.security.networkAdapter":
				from .security_network_adapter import SecurityNetworkAdapter
				return SecurityNetworkAdapter.model_validate(data)
			if mapping_key == "#microsoft.graph.security.policyBase":
				from .security_policy_base import SecurityPolicyBase
				return SecurityPolicyBase.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryHoldPolicy":
				from .security_ediscovery_hold_policy import SecurityEdiscoveryHoldPolicy
				return SecurityEdiscoveryHoldPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.security.protectionRule":
				from .security_protection_rule import SecurityProtectionRule
				return SecurityProtectionRule.model_validate(data)
			if mapping_key == "#microsoft.graph.security.detectionRule":
				from .security_detection_rule import SecurityDetectionRule
				return SecurityDetectionRule.model_validate(data)
			if mapping_key == "#microsoft.graph.security.retentionEvent":
				from .security_retention_event import SecurityRetentionEvent
				return SecurityRetentionEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.security.retentionEventType":
				from .security_retention_event_type import SecurityRetentionEventType
				return SecurityRetentionEventType.model_validate(data)
			if mapping_key == "#microsoft.graph.security.retentionLabel":
				from .security_retention_label import SecurityRetentionLabel
				return SecurityRetentionLabel.model_validate(data)
			if mapping_key == "#microsoft.graph.security.rulesRoot":
				from .security_rules_root import SecurityRulesRoot
				return SecurityRulesRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.security.search":
				from .security_search import SecuritySearch
				return SecuritySearch.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryReviewSetQuery":
				from .security_ediscovery_review_set_query import SecurityEdiscoveryReviewSetQuery
				return SecurityEdiscoveryReviewSetQuery.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoverySearch":
				from .security_ediscovery_search import SecurityEdiscoverySearch
				return SecurityEdiscoverySearch.model_validate(data)
			if mapping_key == "#microsoft.graph.security.security":
				from .security_security import SecuritySecurity
				return SecuritySecurity.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sensitivityLabel":
				from .security_sensitivity_label import SecuritySensitivityLabel
				return SecuritySensitivityLabel.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sensor":
				from .security_sensor import SecuritySensor
				return SecuritySensor.model_validate(data)
			if mapping_key == "#microsoft.graph.security.subdomain":
				from .security_subdomain import SecuritySubdomain
				return SecuritySubdomain.model_validate(data)
			if mapping_key == "#microsoft.graph.security.tag":
				from .security_tag import SecurityTag
				return SecurityTag.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryReviewTag":
				from .security_ediscovery_review_tag import SecurityEdiscoveryReviewTag
				return SecurityEdiscoveryReviewTag.model_validate(data)
			if mapping_key == "#microsoft.graph.security.threatIntelligence":
				from .security_threat_intelligence import SecurityThreatIntelligence
				return SecurityThreatIntelligence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.threatSubmission":
				from .security_threat_submission import SecurityThreatSubmission
				return SecurityThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.emailThreatSubmission":
				from .security_email_threat_submission import SecurityEmailThreatSubmission
				return SecurityEmailThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.emailContentThreatSubmission":
				from .security_email_content_threat_submission import SecurityEmailContentThreatSubmission
				return SecurityEmailContentThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.emailUrlThreatSubmission":
				from .security_email_url_threat_submission import SecurityEmailUrlThreatSubmission
				return SecurityEmailUrlThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.fileThreatSubmission":
				from .security_file_threat_submission import SecurityFileThreatSubmission
				return SecurityFileThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.fileContentThreatSubmission":
				from .security_file_content_threat_submission import SecurityFileContentThreatSubmission
				return SecurityFileContentThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.fileUrlThreatSubmission":
				from .security_file_url_threat_submission import SecurityFileUrlThreatSubmission
				return SecurityFileUrlThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.urlThreatSubmission":
				from .security_url_threat_submission import SecurityUrlThreatSubmission
				return SecurityUrlThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.threatSubmissionRoot":
				from .security_threat_submission_root import SecurityThreatSubmissionRoot
				return SecurityThreatSubmissionRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.security.triggersRoot":
				from .security_triggers_root import SecurityTriggersRoot
				return SecurityTriggersRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.security.triggerTypesRoot":
				from .security_trigger_types_root import SecurityTriggerTypesRoot
				return SecurityTriggerTypesRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vulnerability":
				from .security_vulnerability import SecurityVulnerability
				return SecurityVulnerability.model_validate(data)
			if mapping_key == "#microsoft.graph.security.vulnerabilityComponent":
				from .security_vulnerability_component import SecurityVulnerabilityComponent
				return SecurityVulnerabilityComponent.model_validate(data)
			if mapping_key == "#microsoft.graph.security.whoisBaseRecord":
				from .security_whois_base_record import SecurityWhoisBaseRecord
				return SecurityWhoisBaseRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.whoisHistoryRecord":
				from .security_whois_history_record import SecurityWhoisHistoryRecord
				return SecurityWhoisHistoryRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.security.whoisRecord":
				from .security_whois_record import SecurityWhoisRecord
				return SecurityWhoisRecord.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsAdministration.teamsAdminRoot":
				from .teams_administration_teams_admin_root import TeamsAdministrationTeamsAdminRoot
				return TeamsAdministrationTeamsAdminRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsAdministration.teamsPolicyAssignment":
				from .teams_administration_teams_policy_assignment import TeamsAdministrationTeamsPolicyAssignment
				return TeamsAdministrationTeamsPolicyAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.termStore.group":
				from .term_store_group import TermStoreGroup
				return TermStoreGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.termStore.relation":
				from .term_store_relation import TermStoreRelation
				return TermStoreRelation.model_validate(data)
			if mapping_key == "#microsoft.graph.termStore.set":
				from .term_store_set import TermStoreSet
				return TermStoreSet.model_validate(data)
			if mapping_key == "#microsoft.graph.termStore.store":
				from .term_store_store import TermStoreStore
				return TermStoreStore.model_validate(data)
			if mapping_key == "#microsoft.graph.termStore.term":
				from .term_store_term import TermStoreTerm
				return TermStoreTerm.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.catalog":
				from .windows_updates_catalog import WindowsUpdatesCatalog
				return WindowsUpdatesCatalog.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.catalogEntry":
				from .windows_updates_catalog_entry import WindowsUpdatesCatalogEntry
				return WindowsUpdatesCatalogEntry.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.softwareUpdateCatalogEntry":
				from .windows_updates_software_update_catalog_entry import WindowsUpdatesSoftwareUpdateCatalogEntry
				return WindowsUpdatesSoftwareUpdateCatalogEntry.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.driverUpdateCatalogEntry":
				from .windows_updates_driver_update_catalog_entry import WindowsUpdatesDriverUpdateCatalogEntry
				return WindowsUpdatesDriverUpdateCatalogEntry.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.featureUpdateCatalogEntry":
				from .windows_updates_feature_update_catalog_entry import WindowsUpdatesFeatureUpdateCatalogEntry
				return WindowsUpdatesFeatureUpdateCatalogEntry.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.qualityUpdateCatalogEntry":
				from .windows_updates_quality_update_catalog_entry import WindowsUpdatesQualityUpdateCatalogEntry
				return WindowsUpdatesQualityUpdateCatalogEntry.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.complianceChange":
				from .windows_updates_compliance_change import WindowsUpdatesComplianceChange
				return WindowsUpdatesComplianceChange.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.contentApproval":
				from .windows_updates_content_approval import WindowsUpdatesContentApproval
				return WindowsUpdatesContentApproval.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.deployment":
				from .windows_updates_deployment import WindowsUpdatesDeployment
				return WindowsUpdatesDeployment.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.deploymentAudience":
				from .windows_updates_deployment_audience import WindowsUpdatesDeploymentAudience
				return WindowsUpdatesDeploymentAudience.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.edition":
				from .windows_updates_edition import WindowsUpdatesEdition
				return WindowsUpdatesEdition.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.knowledgeBaseArticle":
				from .windows_updates_knowledge_base_article import WindowsUpdatesKnowledgeBaseArticle
				return WindowsUpdatesKnowledgeBaseArticle.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.knownIssue":
				from .windows_updates_known_issue import WindowsUpdatesKnownIssue
				return WindowsUpdatesKnownIssue.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.product":
				from .windows_updates_product import WindowsUpdatesProduct
				return WindowsUpdatesProduct.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.productRevision":
				from .windows_updates_product_revision import WindowsUpdatesProductRevision
				return WindowsUpdatesProductRevision.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.resourceConnection":
				from .windows_updates_resource_connection import WindowsUpdatesResourceConnection
				return WindowsUpdatesResourceConnection.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.operationalInsightsConnection":
				from .windows_updates_operational_insights_connection import WindowsUpdatesOperationalInsightsConnection
				return WindowsUpdatesOperationalInsightsConnection.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.updatableAsset":
				from .windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset
				return WindowsUpdatesUpdatableAsset.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.azureADDevice":
				from .windows_updates_azure_a_d_device import WindowsUpdatesAzureADDevice
				return WindowsUpdatesAzureADDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.updatableAssetGroup":
				from .windows_updates_updatable_asset_group import WindowsUpdatesUpdatableAssetGroup
				return WindowsUpdatesUpdatableAssetGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.updatePolicy":
				from .windows_updates_update_policy import WindowsUpdatesUpdatePolicy
				return WindowsUpdatesUpdatePolicy.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


