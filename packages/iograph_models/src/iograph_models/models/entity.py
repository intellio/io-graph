from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class Entity(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

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
			if mapping_key == "#microsoft.graph.accessPackageCatalog":
				from .access_package_catalog import AccessPackageCatalog
				return AccessPackageCatalog.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageQuestion":
				from .access_package_question import AccessPackageQuestion
				return AccessPackageQuestion.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageMultipleChoiceQuestion":
				from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
				return AccessPackageMultipleChoiceQuestion.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageTextInputQuestion":
				from .access_package_text_input_question import AccessPackageTextInputQuestion
				return AccessPackageTextInputQuestion.model_validate(data)
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
			if mapping_key == "#microsoft.graph.activityHistoryItem":
				from .activity_history_item import ActivityHistoryItem
				return ActivityHistoryItem.model_validate(data)
			if mapping_key == "#microsoft.graph.adminConsentRequestPolicy":
				from .admin_consent_request_policy import AdminConsentRequestPolicy
				return AdminConsentRequestPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.adminMicrosoft365Apps":
				from .admin_microsoft365_apps import AdminMicrosoft365Apps
				return AdminMicrosoft365Apps.model_validate(data)
			if mapping_key == "#microsoft.graph.adminReportSettings":
				from .admin_report_settings import AdminReportSettings
				return AdminReportSettings.model_validate(data)
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
			if mapping_key == "#microsoft.graph.alert":
				from .alert import Alert
				return Alert.model_validate(data)
			if mapping_key == "#microsoft.graph.allowedValue":
				from .allowed_value import AllowedValue
				return AllowedValue.model_validate(data)
			if mapping_key == "#microsoft.graph.appCatalogs":
				from .app_catalogs import AppCatalogs
				return AppCatalogs.model_validate(data)
			if mapping_key == "#microsoft.graph.appConsentApprovalRoute":
				from .app_consent_approval_route import AppConsentApprovalRoute
				return AppConsentApprovalRoute.model_validate(data)
			if mapping_key == "#microsoft.graph.appConsentRequest":
				from .app_consent_request import AppConsentRequest
				return AppConsentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.applePushNotificationCertificate":
				from .apple_push_notification_certificate import ApplePushNotificationCertificate
				return ApplePushNotificationCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.applicationTemplate":
				from .application_template import ApplicationTemplate
				return ApplicationTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.appLogCollectionRequest":
				from .app_log_collection_request import AppLogCollectionRequest
				return AppLogCollectionRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.approval":
				from .approval import Approval
				return Approval.model_validate(data)
			if mapping_key == "#microsoft.graph.approvalStage":
				from .approval_stage import ApprovalStage
				return ApprovalStage.model_validate(data)
			if mapping_key == "#microsoft.graph.appScope":
				from .app_scope import AppScope
				return AppScope.model_validate(data)
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
			if mapping_key == "#microsoft.graph.auditLogRoot":
				from .audit_log_root import AuditLogRoot
				return AuditLogRoot.model_validate(data)
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
			if mapping_key == "#microsoft.graph.onAuthenticationMethodLoadStartListener":
				from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
				return OnAuthenticationMethodLoadStartListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onInteractiveAuthFlowStartListener":
				from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
				return OnInteractiveAuthFlowStartListener.model_validate(data)
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
			if mapping_key == "#microsoft.graph.authenticationFlowsPolicy":
				from .authentication_flows_policy import AuthenticationFlowsPolicy
				return AuthenticationFlowsPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationMethod":
				from .authentication_method import AuthenticationMethod
				return AuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.emailAuthenticationMethod":
				from .email_authentication_method import EmailAuthenticationMethod
				return EmailAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.fido2AuthenticationMethod":
				from .fido2_authentication_method import Fido2AuthenticationMethod
				return Fido2AuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod":
				from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
				return MicrosoftAuthenticatorAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.passwordAuthenticationMethod":
				from .password_authentication_method import PasswordAuthenticationMethod
				return PasswordAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.phoneAuthenticationMethod":
				from .phone_authentication_method import PhoneAuthenticationMethod
				return PhoneAuthenticationMethod.model_validate(data)
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
			if mapping_key == "#microsoft.graph.fido2AuthenticationMethodConfiguration":
				from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
				return Fido2AuthenticationMethodConfiguration.model_validate(data)
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
			if mapping_key == "#microsoft.graph.smsAuthenticationMethodTarget":
				from .sms_authentication_method_target import SmsAuthenticationMethodTarget
				return SmsAuthenticationMethodTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationStrengthPolicy":
				from .authentication_strength_policy import AuthenticationStrengthPolicy
				return AuthenticationStrengthPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.authenticationStrengthRoot":
				from .authentication_strength_root import AuthenticationStrengthRoot
				return AuthenticationStrengthRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.authoredNote":
				from .authored_note import AuthoredNote
				return AuthoredNote.model_validate(data)
			if mapping_key == "#microsoft.graph.backupRestoreRoot":
				from .backup_restore_root import BackupRestoreRoot
				return BackupRestoreRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.baseItem":
				from .base_item import BaseItem
				return BaseItem.model_validate(data)
			if mapping_key == "#microsoft.graph.baseSitePage":
				from .base_site_page import BaseSitePage
				return BaseSitePage.model_validate(data)
			if mapping_key == "#microsoft.graph.sitePage":
				from .site_page import SitePage
				return SitePage.model_validate(data)
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
			if mapping_key == "#microsoft.graph.bookingBusiness":
				from .booking_business import BookingBusiness
				return BookingBusiness.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingCurrency":
				from .booking_currency import BookingCurrency
				return BookingCurrency.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingCustomerBase":
				from .booking_customer_base import BookingCustomerBase
				return BookingCustomerBase.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingCustomer":
				from .booking_customer import BookingCustomer
				return BookingCustomer.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingCustomQuestion":
				from .booking_custom_question import BookingCustomQuestion
				return BookingCustomQuestion.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingService":
				from .booking_service import BookingService
				return BookingService.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingStaffMemberBase":
				from .booking_staff_member_base import BookingStaffMemberBase
				return BookingStaffMemberBase.model_validate(data)
			if mapping_key == "#microsoft.graph.bookingStaffMember":
				from .booking_staff_member import BookingStaffMember
				return BookingStaffMember.model_validate(data)
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
			if mapping_key == "#microsoft.graph.callRecording":
				from .call_recording import CallRecording
				return CallRecording.model_validate(data)
			if mapping_key == "#microsoft.graph.callTranscript":
				from .call_transcript import CallTranscript
				return CallTranscript.model_validate(data)
			if mapping_key == "#microsoft.graph.canvasLayout":
				from .canvas_layout import CanvasLayout
				return CanvasLayout.model_validate(data)
			if mapping_key == "#microsoft.graph.certificateBasedAuthConfiguration":
				from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
				return CertificateBasedAuthConfiguration.model_validate(data)
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
			if mapping_key == "#microsoft.graph.cloudPcDeviceImage":
				from .cloud_pc_device_image import CloudPcDeviceImage
				return CloudPcDeviceImage.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcGalleryImage":
				from .cloud_pc_gallery_image import CloudPcGalleryImage
				return CloudPcGalleryImage.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcOnPremisesConnection":
				from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
				return CloudPcOnPremisesConnection.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcProvisioningPolicy":
				from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
				return CloudPcProvisioningPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcProvisioningPolicyAssignment":
				from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
				return CloudPcProvisioningPolicyAssignment.model_validate(data)
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
			if mapping_key == "#microsoft.graph.stopHoldMusicOperation":
				from .stop_hold_music_operation import StopHoldMusicOperation
				return StopHoldMusicOperation.model_validate(data)
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
			if mapping_key == "#microsoft.graph.conditionalAccessRoot":
				from .conditional_access_root import ConditionalAccessRoot
				return ConditionalAccessRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.conditionalAccessTemplate":
				from .conditional_access_template import ConditionalAccessTemplate
				return ConditionalAccessTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.connectedOrganization":
				from .connected_organization import ConnectedOrganization
				return ConnectedOrganization.model_validate(data)
			if mapping_key == "#microsoft.graph.contactFolder":
				from .contact_folder import ContactFolder
				return ContactFolder.model_validate(data)
			if mapping_key == "#microsoft.graph.contentSharingSession":
				from .content_sharing_session import ContentSharingSession
				return ContentSharingSession.model_validate(data)
			if mapping_key == "#microsoft.graph.contentType":
				from .content_type import ContentType
				return ContentType.model_validate(data)
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
			if mapping_key == "#microsoft.graph.customAuthenticationExtension":
				from .custom_authentication_extension import CustomAuthenticationExtension
				return CustomAuthenticationExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.onTokenIssuanceStartCustomExtension":
				from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
				return OnTokenIssuanceStartCustomExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.customTaskExtension":
				from .identity_governance_custom_task_extension import IdentityGovernanceCustomTaskExtension
				return IdentityGovernanceCustomTaskExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.customExtensionStageSetting":
				from .custom_extension_stage_setting import CustomExtensionStageSetting
				return CustomExtensionStageSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.customSecurityAttributeDefinition":
				from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
				return CustomSecurityAttributeDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.dataPolicyOperation":
				from .data_policy_operation import DataPolicyOperation
				return DataPolicyOperation.model_validate(data)
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
			if mapping_key == "#microsoft.graph.detectedApp":
				from .detected_app import DetectedApp
				return DetectedApp.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceAppManagement":
				from .device_app_management import DeviceAppManagement
				return DeviceAppManagement.model_validate(data)
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
			if mapping_key == "#microsoft.graph.androidWorkProfileCompliancePolicy":
				from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
				return AndroidWorkProfileCompliancePolicy.model_validate(data)
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
			if mapping_key == "#microsoft.graph.deviceCompliancePolicySettingStateSummary":
				from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
				return DeviceCompliancePolicySettingStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceCompliancePolicyState":
				from .device_compliance_policy_state import DeviceCompliancePolicyState
				return DeviceCompliancePolicyState.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceComplianceScheduledActionForRule":
				from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
				return DeviceComplianceScheduledActionForRule.model_validate(data)
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
			if mapping_key == "#microsoft.graph.androidCustomConfiguration":
				from .android_custom_configuration import AndroidCustomConfiguration
				return AndroidCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidGeneralDeviceConfiguration":
				from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
				return AndroidGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileCustomConfiguration":
				from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
				return AndroidWorkProfileCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration":
				from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
				return AndroidWorkProfileGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.appleDeviceFeaturesConfigurationBase":
				from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
				return AppleDeviceFeaturesConfigurationBase.model_validate(data)
			if mapping_key == "#microsoft.graph.iosDeviceFeaturesConfiguration":
				from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
				return IosDeviceFeaturesConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSDeviceFeaturesConfiguration":
				from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
				return MacOSDeviceFeaturesConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.editionUpgradeConfiguration":
				from .edition_upgrade_configuration import EditionUpgradeConfiguration
				return EditionUpgradeConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosCertificateProfile":
				from .ios_certificate_profile import IosCertificateProfile
				return IosCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.iosCustomConfiguration":
				from .ios_custom_configuration import IosCustomConfiguration
				return IosCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosGeneralDeviceConfiguration":
				from .ios_general_device_configuration import IosGeneralDeviceConfiguration
				return IosGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosUpdateConfiguration":
				from .ios_update_configuration import IosUpdateConfiguration
				return IosUpdateConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSCustomConfiguration":
				from .mac_o_s_custom_configuration import MacOSCustomConfiguration
				return MacOSCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSGeneralDeviceConfiguration":
				from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
				return MacOSGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedPCConfiguration":
				from .shared_p_c_configuration import SharedPCConfiguration
				return SharedPCConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10CustomConfiguration":
				from .windows10_custom_configuration import Windows10CustomConfiguration
				return Windows10CustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EndpointProtectionConfiguration":
				from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
				return Windows10EndpointProtectionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration":
				from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
				return Windows10EnterpriseModernAppManagementConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10GeneralConfiguration":
				from .windows10_general_configuration import Windows10GeneralConfiguration
				return Windows10GeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10SecureAssessmentConfiguration":
				from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
				return Windows10SecureAssessmentConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10TeamGeneralConfiguration":
				from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
				return Windows10TeamGeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81GeneralConfiguration":
				from .windows81_general_configuration import Windows81GeneralConfiguration
				return Windows81GeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration":
				from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
				return WindowsDefenderAdvancedThreatProtectionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81CustomConfiguration":
				from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
				return WindowsPhone81CustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81GeneralConfiguration":
				from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
				return WindowsPhone81GeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdateForBusinessConfiguration":
				from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
				return WindowsUpdateForBusinessConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationAssignment":
				from .device_configuration_assignment import DeviceConfigurationAssignment
				return DeviceConfigurationAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationDeviceOverview":
				from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
				return DeviceConfigurationDeviceOverview.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationDeviceStateSummary":
				from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
				return DeviceConfigurationDeviceStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationDeviceStatus":
				from .device_configuration_device_status import DeviceConfigurationDeviceStatus
				return DeviceConfigurationDeviceStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationState":
				from .device_configuration_state import DeviceConfigurationState
				return DeviceConfigurationState.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationUserOverview":
				from .device_configuration_user_overview import DeviceConfigurationUserOverview
				return DeviceConfigurationUserOverview.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationUserStatus":
				from .device_configuration_user_status import DeviceConfigurationUserStatus
				return DeviceConfigurationUserStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceEnrollmentConfiguration":
				from .device_enrollment_configuration import DeviceEnrollmentConfiguration
				return DeviceEnrollmentConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceEnrollmentLimitConfiguration":
				from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
				return DeviceEnrollmentLimitConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration":
				from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
				return DeviceEnrollmentPlatformRestrictionsConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceEnrollmentWindowsHelloForBusinessConfiguration":
				from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
				return DeviceEnrollmentWindowsHelloForBusinessConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EnrollmentCompletionPageConfiguration":
				from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration
				return Windows10EnrollmentCompletionPageConfiguration.model_validate(data)
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
			if mapping_key == "#microsoft.graph.deviceManagementCachedReportConfiguration":
				from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration
				return DeviceManagementCachedReportConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementExchangeConnector":
				from .device_management_exchange_connector import DeviceManagementExchangeConnector
				return DeviceManagementExchangeConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementExportJob":
				from .device_management_export_job import DeviceManagementExportJob
				return DeviceManagementExportJob.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementPartner":
				from .device_management_partner import DeviceManagementPartner
				return DeviceManagementPartner.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementReports":
				from .device_management_reports import DeviceManagementReports
				return DeviceManagementReports.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementTroubleshootingEvent":
				from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
				return DeviceManagementTroubleshootingEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.enrollmentTroubleshootingEvent":
				from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
				return EnrollmentTroubleshootingEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceRegistrationPolicy":
				from .device_registration_policy import DeviceRegistrationPolicy
				return DeviceRegistrationPolicy.model_validate(data)
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
			if mapping_key == "#microsoft.graph.contract":
				from .contract import Contract
				return Contract.model_validate(data)
			if mapping_key == "#microsoft.graph.device":
				from .device import Device
				return Device.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryObjectPartnerReference":
				from .directory_object_partner_reference import DirectoryObjectPartnerReference
				return DirectoryObjectPartnerReference.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryRole":
				from .directory_role import DirectoryRole
				return DirectoryRole.model_validate(data)
			if mapping_key == "#microsoft.graph.directoryRoleTemplate":
				from .directory_role_template import DirectoryRoleTemplate
				return DirectoryRoleTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.endpoint":
				from .endpoint import Endpoint
				return Endpoint.model_validate(data)
			if mapping_key == "#microsoft.graph.extensionProperty":
				from .extension_property import ExtensionProperty
				return ExtensionProperty.model_validate(data)
			if mapping_key == "#microsoft.graph.group":
				from .group import Group
				return Group.model_validate(data)
			if mapping_key == "#microsoft.graph.groupSettingTemplate":
				from .group_setting_template import GroupSettingTemplate
				return GroupSettingTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.multiTenantOrganizationMember":
				from .multi_tenant_organization_member import MultiTenantOrganizationMember
				return MultiTenantOrganizationMember.model_validate(data)
			if mapping_key == "#microsoft.graph.organization":
				from .organization import Organization
				return Organization.model_validate(data)
			if mapping_key == "#microsoft.graph.orgContact":
				from .org_contact import OrgContact
				return OrgContact.model_validate(data)
			if mapping_key == "#microsoft.graph.policyBase":
				from .policy_base import PolicyBase
				return PolicyBase.model_validate(data)
			if mapping_key == "#microsoft.graph.appManagementPolicy":
				from .app_management_policy import AppManagementPolicy
				return AppManagementPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.authorizationPolicy":
				from .authorization_policy import AuthorizationPolicy
				return AuthorizationPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.crossTenantAccessPolicy":
				from .cross_tenant_access_policy import CrossTenantAccessPolicy
				return CrossTenantAccessPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy":
				from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
				return IdentitySecurityDefaultsEnforcementPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionGrantPolicy":
				from .permission_grant_policy import PermissionGrantPolicy
				return PermissionGrantPolicy.model_validate(data)
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
			if mapping_key == "#microsoft.graph.resourceSpecificPermissionGrant":
				from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
				return ResourceSpecificPermissionGrant.model_validate(data)
			if mapping_key == "#microsoft.graph.servicePrincipal":
				from .service_principal import ServicePrincipal
				return ServicePrincipal.model_validate(data)
			if mapping_key == "#microsoft.graph.user":
				from .user import User
				return User.model_validate(data)
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
			if mapping_key == "#microsoft.graph.employeeExperienceUser":
				from .employee_experience_user import EmployeeExperienceUser
				return EmployeeExperienceUser.model_validate(data)
			if mapping_key == "#microsoft.graph.endUserNotification":
				from .end_user_notification import EndUserNotification
				return EndUserNotification.model_validate(data)
			if mapping_key == "#microsoft.graph.endUserNotificationDetail":
				from .end_user_notification_detail import EndUserNotificationDetail
				return EndUserNotificationDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.enrollmentConfigurationAssignment":
				from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
				return EnrollmentConfigurationAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.enterpriseCodeSigningCertificate":
				from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
				return EnterpriseCodeSigningCertificate.model_validate(data)
			if mapping_key == "#microsoft.graph.entitlementManagement":
				from .entitlement_management import EntitlementManagement
				return EntitlementManagement.model_validate(data)
			if mapping_key == "#microsoft.graph.entitlementManagementSettings":
				from .entitlement_management_settings import EntitlementManagementSettings
				return EntitlementManagementSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.extension":
				from .extension import Extension
				return Extension.model_validate(data)
			if mapping_key == "#microsoft.graph.openTypeExtension":
				from .open_type_extension import OpenTypeExtension
				return OpenTypeExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.externalDomainName":
				from .external_domain_name import ExternalDomainName
				return ExternalDomainName.model_validate(data)
			if mapping_key == "#microsoft.graph.featureRolloutPolicy":
				from .feature_rollout_policy import FeatureRolloutPolicy
				return FeatureRolloutPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.federatedIdentityCredential":
				from .federated_identity_credential import FederatedIdentityCredential
				return FederatedIdentityCredential.model_validate(data)
			if mapping_key == "#microsoft.graph.fieldValueSet":
				from .field_value_set import FieldValueSet
				return FieldValueSet.model_validate(data)
			if mapping_key == "#microsoft.graph.fileStorage":
				from .file_storage import FileStorage
				return FileStorage.model_validate(data)
			if mapping_key == "#microsoft.graph.fileStorageContainer":
				from .file_storage_container import FileStorageContainer
				return FileStorageContainer.model_validate(data)
			if mapping_key == "#microsoft.graph.filterOperatorSchema":
				from .filter_operator_schema import FilterOperatorSchema
				return FilterOperatorSchema.model_validate(data)
			if mapping_key == "#microsoft.graph.governanceInsight":
				from .governance_insight import GovernanceInsight
				return GovernanceInsight.model_validate(data)
			if mapping_key == "#microsoft.graph.membershipOutlierInsight":
				from .membership_outlier_insight import MembershipOutlierInsight
				return MembershipOutlierInsight.model_validate(data)
			if mapping_key == "#microsoft.graph.userSignInInsight":
				from .user_sign_in_insight import UserSignInInsight
				return UserSignInInsight.model_validate(data)
			if mapping_key == "#microsoft.graph.groupLifecyclePolicy":
				from .group_lifecycle_policy import GroupLifecyclePolicy
				return GroupLifecyclePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.groupSetting":
				from .group_setting import GroupSetting
				return GroupSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.horizontalSection":
				from .horizontal_section import HorizontalSection
				return HorizontalSection.model_validate(data)
			if mapping_key == "#microsoft.graph.horizontalSectionColumn":
				from .horizontal_section_column import HorizontalSectionColumn
				return HorizontalSectionColumn.model_validate(data)
			if mapping_key == "#microsoft.graph.identityApiConnector":
				from .identity_api_connector import IdentityApiConnector
				return IdentityApiConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.identityContainer":
				from .identity_container import IdentityContainer
				return IdentityContainer.model_validate(data)
			if mapping_key == "#microsoft.graph.identityProvider":
				from .identity_provider import IdentityProvider
				return IdentityProvider.model_validate(data)
			if mapping_key == "#microsoft.graph.identityProviderBase":
				from .identity_provider_base import IdentityProviderBase
				return IdentityProviderBase.model_validate(data)
			if mapping_key == "#microsoft.graph.appleManagedIdentityProvider":
				from .apple_managed_identity_provider import AppleManagedIdentityProvider
				return AppleManagedIdentityProvider.model_validate(data)
			if mapping_key == "#microsoft.graph.builtInIdentityProvider":
				from .built_in_identity_provider import BuiltInIdentityProvider
				return BuiltInIdentityProvider.model_validate(data)
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
			if mapping_key == "#microsoft.graph.importedWindowsAutopilotDeviceIdentity":
				from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
				return ImportedWindowsAutopilotDeviceIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.importedWindowsAutopilotDeviceIdentityUpload":
				from .imported_windows_autopilot_device_identity_upload import ImportedWindowsAutopilotDeviceIdentityUpload
				return ImportedWindowsAutopilotDeviceIdentityUpload.model_validate(data)
			if mapping_key == "#microsoft.graph.inferenceClassification":
				from .inference_classification import InferenceClassification
				return InferenceClassification.model_validate(data)
			if mapping_key == "#microsoft.graph.inferenceClassificationOverride":
				from .inference_classification_override import InferenceClassificationOverride
				return InferenceClassificationOverride.model_validate(data)
			if mapping_key == "#microsoft.graph.insightsSettings":
				from .insights_settings import InsightsSettings
				return InsightsSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.internetExplorerMode":
				from .internet_explorer_mode import InternetExplorerMode
				return InternetExplorerMode.model_validate(data)
			if mapping_key == "#microsoft.graph.invitation":
				from .invitation import Invitation
				return Invitation.model_validate(data)
			if mapping_key == "#microsoft.graph.iosLobAppProvisioningConfigurationAssignment":
				from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
				return IosLobAppProvisioningConfigurationAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.iosUpdateDeviceStatus":
				from .ios_update_device_status import IosUpdateDeviceStatus
				return IosUpdateDeviceStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.itemActivity":
				from .item_activity import ItemActivity
				return ItemActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.itemActivityStat":
				from .item_activity_stat import ItemActivityStat
				return ItemActivityStat.model_validate(data)
			if mapping_key == "#microsoft.graph.itemAnalytics":
				from .item_analytics import ItemAnalytics
				return ItemAnalytics.model_validate(data)
			if mapping_key == "#microsoft.graph.itemRetentionLabel":
				from .item_retention_label import ItemRetentionLabel
				return ItemRetentionLabel.model_validate(data)
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
			if mapping_key == "#microsoft.graph.richLongRunningOperation":
				from .rich_long_running_operation import RichLongRunningOperation
				return RichLongRunningOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.m365AppsInstallationOptions":
				from .m365_apps_installation_options import M365AppsInstallationOptions
				return M365AppsInstallationOptions.model_validate(data)
			if mapping_key == "#microsoft.graph.mailFolder":
				from .mail_folder import MailFolder
				return MailFolder.model_validate(data)
			if mapping_key == "#microsoft.graph.mailSearchFolder":
				from .mail_search_folder import MailSearchFolder
				return MailSearchFolder.model_validate(data)
			if mapping_key == "#microsoft.graph.malwareStateForWindowsDevice":
				from .malware_state_for_windows_device import MalwareStateForWindowsDevice
				return MalwareStateForWindowsDevice.model_validate(data)
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
			if mapping_key == "#microsoft.graph.managedAppStatus":
				from .managed_app_status import ManagedAppStatus
				return ManagedAppStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppStatusRaw":
				from .managed_app_status_raw import ManagedAppStatusRaw
				return ManagedAppStatusRaw.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDevice":
				from .managed_device import ManagedDevice
				return ManagedDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceMobileAppConfiguration":
				from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
				return ManagedDeviceMobileAppConfiguration.model_validate(data)
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
			if mapping_key == "#microsoft.graph.managedDeviceMobileAppConfigurationUserStatus":
				from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
				return ManagedDeviceMobileAppConfigurationUserStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceMobileAppConfigurationUserSummary":
				from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary
				return ManagedDeviceMobileAppConfigurationUserSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceOverview":
				from .managed_device_overview import ManagedDeviceOverview
				return ManagedDeviceOverview.model_validate(data)
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
			if mapping_key == "#microsoft.graph.managedMobileApp":
				from .managed_mobile_app import ManagedMobileApp
				return ManagedMobileApp.model_validate(data)
			if mapping_key == "#microsoft.graph.meetingAttendanceReport":
				from .meeting_attendance_report import MeetingAttendanceReport
				return MeetingAttendanceReport.model_validate(data)
			if mapping_key == "#microsoft.graph.messageRule":
				from .message_rule import MessageRule
				return MessageRule.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileApp":
				from .mobile_app import MobileApp
				return MobileApp.model_validate(data)
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
			if mapping_key == "#microsoft.graph.win32LobApp":
				from .win32_lob_app import Win32LobApp
				return Win32LobApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAppX":
				from .windows_app_x import WindowsAppX
				return WindowsAppX.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsMobileMSI":
				from .windows_mobile_m_s_i import WindowsMobileMSI
				return WindowsMobileMSI.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUniversalAppX":
				from .windows_universal_app_x import WindowsUniversalAppX
				return WindowsUniversalAppX.model_validate(data)
			if mapping_key == "#microsoft.graph.webApp":
				from .web_app import WebApp
				return WebApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsMicrosoftEdgeApp":
				from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
				return WindowsMicrosoftEdgeApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsWebApp":
				from .windows_web_app import WindowsWebApp
				return WindowsWebApp.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppAssignment":
				from .mobile_app_assignment import MobileAppAssignment
				return MobileAppAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppCategory":
				from .mobile_app_category import MobileAppCategory
				return MobileAppCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppContent":
				from .mobile_app_content import MobileAppContent
				return MobileAppContent.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppContentFile":
				from .mobile_app_content_file import MobileAppContentFile
				return MobileAppContentFile.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppTroubleshootingEvent":
				from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
				return MobileAppTroubleshootingEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileContainedApp":
				from .mobile_contained_app import MobileContainedApp
				return MobileContainedApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUniversalAppXContainedApp":
				from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp
				return WindowsUniversalAppXContainedApp.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileThreatDefenseConnector":
				from .mobile_threat_defense_connector import MobileThreatDefenseConnector
				return MobileThreatDefenseConnector.model_validate(data)
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
			if mapping_key == "#microsoft.graph.countryNamedLocation":
				from .country_named_location import CountryNamedLocation
				return CountryNamedLocation.model_validate(data)
			if mapping_key == "#microsoft.graph.ipNamedLocation":
				from .ip_named_location import IpNamedLocation
				return IpNamedLocation.model_validate(data)
			if mapping_key == "#microsoft.graph.notificationMessageTemplate":
				from .notification_message_template import NotificationMessageTemplate
				return NotificationMessageTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.oAuth2PermissionGrant":
				from .o_auth2_permission_grant import OAuth2PermissionGrant
				return OAuth2PermissionGrant.model_validate(data)
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
			if mapping_key == "#microsoft.graph.onPremisesConditionalAccessSettings":
				from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
				return OnPremisesConditionalAccessSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.onPremisesDirectorySynchronization":
				from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
				return OnPremisesDirectorySynchronization.model_validate(data)
			if mapping_key == "#microsoft.graph.operation":
				from .operation import Operation
				return Operation.model_validate(data)
			if mapping_key == "#microsoft.graph.onenoteOperation":
				from .onenote_operation import OnenoteOperation
				return OnenoteOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.organizationalBrandingProperties":
				from .organizational_branding_properties import OrganizationalBrandingProperties
				return OrganizationalBrandingProperties.model_validate(data)
			if mapping_key == "#microsoft.graph.organizationalBranding":
				from .organizational_branding import OrganizationalBranding
				return OrganizationalBranding.model_validate(data)
			if mapping_key == "#microsoft.graph.organizationalBrandingLocalization":
				from .organizational_branding_localization import OrganizationalBrandingLocalization
				return OrganizationalBrandingLocalization.model_validate(data)
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
			if mapping_key == "#microsoft.graph.post":
				from .post import Post
				return Post.model_validate(data)
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
			if mapping_key == "#microsoft.graph.peopleAdminSettings":
				from .people_admin_settings import PeopleAdminSettings
				return PeopleAdminSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.permission":
				from .permission import Permission
				return Permission.model_validate(data)
			if mapping_key == "#microsoft.graph.permissionGrantConditionSet":
				from .permission_grant_condition_set import PermissionGrantConditionSet
				return PermissionGrantConditionSet.model_validate(data)
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
			if mapping_key == "#microsoft.graph.planner":
				from .planner import Planner
				return Planner.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerAssignedToTaskBoardTaskFormat":
				from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
				return PlannerAssignedToTaskBoardTaskFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerBucket":
				from .planner_bucket import PlannerBucket
				return PlannerBucket.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerBucketTaskBoardTaskFormat":
				from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
				return PlannerBucketTaskBoardTaskFormat.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerGroup":
				from .planner_group import PlannerGroup
				return PlannerGroup.model_validate(data)
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
			if mapping_key == "#microsoft.graph.plannerTaskDetails":
				from .planner_task_details import PlannerTaskDetails
				return PlannerTaskDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.plannerUser":
				from .planner_user import PlannerUser
				return PlannerUser.model_validate(data)
			if mapping_key == "#microsoft.graph.policyRoot":
				from .policy_root import PolicyRoot
				return PolicyRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.policyTemplate":
				from .policy_template import PolicyTemplate
				return PolicyTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.presence":
				from .presence import Presence
				return Presence.model_validate(data)
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
			if mapping_key == "#microsoft.graph.profileCardProperty":
				from .profile_card_property import ProfileCardProperty
				return ProfileCardProperty.model_validate(data)
			if mapping_key == "#microsoft.graph.profilePhoto":
				from .profile_photo import ProfilePhoto
				return ProfilePhoto.model_validate(data)
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
			if mapping_key == "#microsoft.graph.provisioningObjectSummary":
				from .provisioning_object_summary import ProvisioningObjectSummary
				return ProvisioningObjectSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.rbacApplication":
				from .rbac_application import RbacApplication
				return RbacApplication.model_validate(data)
			if mapping_key == "#microsoft.graph.relyingPartyDetailedSummary":
				from .relying_party_detailed_summary import RelyingPartyDetailedSummary
				return RelyingPartyDetailedSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.remoteAssistancePartner":
				from .remote_assistance_partner import RemoteAssistancePartner
				return RemoteAssistancePartner.model_validate(data)
			if mapping_key == "#microsoft.graph.remoteDesktopSecurityConfiguration":
				from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
				return RemoteDesktopSecurityConfiguration.model_validate(data)
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
			if mapping_key == "#microsoft.graph.schedule":
				from .schedule import Schedule
				return Schedule.model_validate(data)
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
			if mapping_key == "#microsoft.graph.security":
				from .security import Security
				return Security.model_validate(data)
			if mapping_key == "#microsoft.graph.securityReportsRoot":
				from .security_reports_root import SecurityReportsRoot
				return SecurityReportsRoot.model_validate(data)
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
			if mapping_key == "#microsoft.graph.servicePrincipalRiskDetection":
				from .service_principal_risk_detection import ServicePrincipalRiskDetection
				return ServicePrincipalRiskDetection.model_validate(data)
			if mapping_key == "#microsoft.graph.settingStateDeviceSummary":
				from .setting_state_device_summary import SettingStateDeviceSummary
				return SettingStateDeviceSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedInsight":
				from .shared_insight import SharedInsight
				return SharedInsight.model_validate(data)
			if mapping_key == "#microsoft.graph.sharepoint":
				from .sharepoint import Sharepoint
				return Sharepoint.model_validate(data)
			if mapping_key == "#microsoft.graph.sharepointSettings":
				from .sharepoint_settings import SharepointSettings
				return SharepointSettings.model_validate(data)
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
			if mapping_key == "#microsoft.graph.subjectRightsRequest":
				from .subject_rights_request import SubjectRightsRequest
				return SubjectRightsRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.subscribedSku":
				from .subscribed_sku import SubscribedSku
				return SubscribedSku.model_validate(data)
			if mapping_key == "#microsoft.graph.subscription":
				from .subscription import Subscription
				return Subscription.model_validate(data)
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
			if mapping_key == "#microsoft.graph.teamsAppDefinition":
				from .teams_app_definition import TeamsAppDefinition
				return TeamsAppDefinition.model_validate(data)
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
			if mapping_key == "#microsoft.graph.teamsTab":
				from .teams_tab import TeamsTab
				return TeamsTab.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsTemplate":
				from .teams_template import TeamsTemplate
				return TeamsTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.teamwork":
				from .teamwork import Teamwork
				return Teamwork.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkBot":
				from .teamwork_bot import TeamworkBot
				return TeamworkBot.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkHostedContent":
				from .teamwork_hosted_content import TeamworkHostedContent
				return TeamworkHostedContent.model_validate(data)
			if mapping_key == "#microsoft.graph.chatMessageHostedContent":
				from .chat_message_hosted_content import ChatMessageHostedContent
				return ChatMessageHostedContent.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkTag":
				from .teamwork_tag import TeamworkTag
				return TeamworkTag.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkTagMember":
				from .teamwork_tag_member import TeamworkTagMember
				return TeamworkTagMember.model_validate(data)
			if mapping_key == "#microsoft.graph.telecomExpenseManagementPartner":
				from .telecom_expense_management_partner import TelecomExpenseManagementPartner
				return TelecomExpenseManagementPartner.model_validate(data)
			if mapping_key == "#microsoft.graph.termsAndConditions":
				from .terms_and_conditions import TermsAndConditions
				return TermsAndConditions.model_validate(data)
			if mapping_key == "#microsoft.graph.termsAndConditionsAcceptanceStatus":
				from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
				return TermsAndConditionsAcceptanceStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.termsAndConditionsAssignment":
				from .terms_and_conditions_assignment import TermsAndConditionsAssignment
				return TermsAndConditionsAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.termsOfUseContainer":
				from .terms_of_use_container import TermsOfUseContainer
				return TermsOfUseContainer.model_validate(data)
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
			if mapping_key == "#microsoft.graph.trainingLanguageDetail":
				from .training_language_detail import TrainingLanguageDetail
				return TrainingLanguageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.trending":
				from .trending import Trending
				return Trending.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRbacResourceAction":
				from .unified_rbac_resource_action import UnifiedRbacResourceAction
				return UnifiedRbacResourceAction.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRbacResourceNamespace":
				from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
				return UnifiedRbacResourceNamespace.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleAssignment":
				from .unified_role_assignment import UnifiedRoleAssignment
				return UnifiedRoleAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleDefinition":
				from .unified_role_definition import UnifiedRoleDefinition
				return UnifiedRoleDefinition.model_validate(data)
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
			if mapping_key == "#microsoft.graph.usedInsight":
				from .used_insight import UsedInsight
				return UsedInsight.model_validate(data)
			if mapping_key == "#microsoft.graph.userActivity":
				from .user_activity import UserActivity
				return UserActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsAppHealthApplicationPerformance":
				from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
				return UserExperienceAnalyticsAppHealthApplicationPerformance.model_validate(data)
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
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsCategory":
				from .user_experience_analytics_category import UserExperienceAnalyticsCategory
				return UserExperienceAnalyticsCategory.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsDevicePerformance":
				from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
				return UserExperienceAnalyticsDevicePerformance.model_validate(data)
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
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsMetric":
				from .user_experience_analytics_metric import UserExperienceAnalyticsMetric
				return UserExperienceAnalyticsMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsMetricHistory":
				from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
				return UserExperienceAnalyticsMetricHistory.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsModelScores":
				from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
				return UserExperienceAnalyticsModelScores.model_validate(data)
			if mapping_key == "#microsoft.graph.userExperienceAnalyticsOverview":
				from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
				return UserExperienceAnalyticsOverview.model_validate(data)
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
			if mapping_key == "#microsoft.graph.userInsightsSettings":
				from .user_insights_settings import UserInsightsSettings
				return UserInsightsSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.userInstallStateSummary":
				from .user_install_state_summary import UserInstallStateSummary
				return UserInstallStateSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.userRegistrationDetails":
				from .user_registration_details import UserRegistrationDetails
				return UserRegistrationDetails.model_validate(data)
			if mapping_key == "#microsoft.graph.userSettings":
				from .user_settings import UserSettings
				return UserSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.userSolutionRoot":
				from .user_solution_root import UserSolutionRoot
				return UserSolutionRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.userStorage":
				from .user_storage import UserStorage
				return UserStorage.model_validate(data)
			if mapping_key == "#microsoft.graph.userTeamwork":
				from .user_teamwork import UserTeamwork
				return UserTeamwork.model_validate(data)
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
			if mapping_key == "#microsoft.graph.vppToken":
				from .vpp_token import VppToken
				return VppToken.model_validate(data)
			if mapping_key == "#microsoft.graph.webPart":
				from .web_part import WebPart
				return WebPart.model_validate(data)
			if mapping_key == "#microsoft.graph.standardWebPart":
				from .standard_web_part import StandardWebPart
				return StandardWebPart.model_validate(data)
			if mapping_key == "#microsoft.graph.textWebPart":
				from .text_web_part import TextWebPart
				return TextWebPart.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAutopilotDeploymentProfile":
				from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
				return WindowsAutopilotDeploymentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAutopilotDeploymentProfileAssignment":
				from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
				return WindowsAutopilotDeploymentProfileAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAutopilotDeviceIdentity":
				from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
				return WindowsAutopilotDeviceIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDeviceMalwareState":
				from .windows_device_malware_state import WindowsDeviceMalwareState
				return WindowsDeviceMalwareState.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtectionAppLearningSummary":
				from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
				return WindowsInformationProtectionAppLearningSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtectionAppLockerFile":
				from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
				return WindowsInformationProtectionAppLockerFile.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtectionNetworkLearningSummary":
				from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
				return WindowsInformationProtectionNetworkLearningSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsMalwareInformation":
				from .windows_malware_information import WindowsMalwareInformation
				return WindowsMalwareInformation.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsProtectionState":
				from .windows_protection_state import WindowsProtectionState
				return WindowsProtectionState.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsSetting":
				from .windows_setting import WindowsSetting
				return WindowsSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsSettingInstance":
				from .windows_setting_instance import WindowsSettingInstance
				return WindowsSettingInstance.model_validate(data)
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
			if mapping_key == "#microsoft.graph.externalConnectors.connectionOperation":
				from .external_connectors_connection_operation import ExternalConnectorsConnectionOperation
				return ExternalConnectorsConnectionOperation.model_validate(data)
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
			if mapping_key == "#microsoft.graph.security.dispositionReviewStage":
				from .security_disposition_review_stage import SecurityDispositionReviewStage
				return SecurityDispositionReviewStage.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryCaseSettings":
				from .security_ediscovery_case_settings import SecurityEdiscoveryCaseSettings
				return SecurityEdiscoveryCaseSettings.model_validate(data)
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
			if mapping_key == "#microsoft.graph.security.intelligenceProfile":
				from .security_intelligence_profile import SecurityIntelligenceProfile
				return SecurityIntelligenceProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.security.labelsRoot":
				from .security_labels_root import SecurityLabelsRoot
				return SecurityLabelsRoot.model_validate(data)
			if mapping_key == "#microsoft.graph.security.networkAdapter":
				from .security_network_adapter import SecurityNetworkAdapter
				return SecurityNetworkAdapter.model_validate(data)
			if mapping_key == "#microsoft.graph.security.retentionEvent":
				from .security_retention_event import SecurityRetentionEvent
				return SecurityRetentionEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.security.retentionEventType":
				from .security_retention_event_type import SecurityRetentionEventType
				return SecurityRetentionEventType.model_validate(data)
			if mapping_key == "#microsoft.graph.security.retentionLabel":
				from .security_retention_label import SecurityRetentionLabel
				return SecurityRetentionLabel.model_validate(data)
			if mapping_key == "#microsoft.graph.security.search":
				from .security_search import SecuritySearch
				return SecuritySearch.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryReviewSetQuery":
				from .security_ediscovery_review_set_query import SecurityEdiscoveryReviewSetQuery
				return SecurityEdiscoveryReviewSetQuery.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoverySearch":
				from .security_ediscovery_search import SecurityEdiscoverySearch
				return SecurityEdiscoverySearch.model_validate(data)
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
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


