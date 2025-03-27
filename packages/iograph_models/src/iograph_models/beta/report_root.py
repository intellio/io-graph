from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class ReportRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appCredentialSignInActivities: Optional[list[AppCredentialSignInActivity]] = Field(alias="appCredentialSignInActivities", default=None,)
	applicationSignInDetailedSummary: Optional[list[ApplicationSignInDetailedSummary]] = Field(alias="applicationSignInDetailedSummary", default=None,)
	authenticationMethods: Optional[AuthenticationMethodsRoot] = Field(alias="authenticationMethods", default=None,)
	credentialUserRegistrationDetails: Optional[list[CredentialUserRegistrationDetails]] = Field(alias="credentialUserRegistrationDetails", default=None,)
	dailyPrintUsage: Optional[list[Annotated[Union[PrintUsageByPrinter, PrintUsageByUser],Field(discriminator="odata_type")]]] = Field(alias="dailyPrintUsage", default=None,)
	dailyPrintUsageByPrinter: Optional[list[PrintUsageByPrinter]] = Field(alias="dailyPrintUsageByPrinter", default=None,)
	dailyPrintUsageByUser: Optional[list[PrintUsageByUser]] = Field(alias="dailyPrintUsageByUser", default=None,)
	dailyPrintUsageSummariesByPrinter: Optional[list[PrintUsageByPrinter]] = Field(alias="dailyPrintUsageSummariesByPrinter", default=None,)
	dailyPrintUsageSummariesByUser: Optional[list[PrintUsageByUser]] = Field(alias="dailyPrintUsageSummariesByUser", default=None,)
	healthMonitoring: Optional[HealthMonitoringHealthMonitoringRoot] = Field(alias="healthMonitoring", default=None,)
	monthlyPrintUsageByPrinter: Optional[list[PrintUsageByPrinter]] = Field(alias="monthlyPrintUsageByPrinter", default=None,)
	monthlyPrintUsageByUser: Optional[list[PrintUsageByUser]] = Field(alias="monthlyPrintUsageByUser", default=None,)
	monthlyPrintUsageSummariesByPrinter: Optional[list[PrintUsageByPrinter]] = Field(alias="monthlyPrintUsageSummariesByPrinter", default=None,)
	monthlyPrintUsageSummariesByUser: Optional[list[PrintUsageByUser]] = Field(alias="monthlyPrintUsageSummariesByUser", default=None,)
	partners: Optional[Partners] = Field(alias="partners", default=None,)
	security: Optional[SecurityReportsRoot] = Field(alias="security", default=None,)
	serviceActivity: Optional[ServiceActivity] = Field(alias="serviceActivity", default=None,)
	servicePrincipalSignInActivities: Optional[list[ServicePrincipalSignInActivity]] = Field(alias="servicePrincipalSignInActivities", default=None,)
	sla: Optional[ServiceLevelAgreementRoot] = Field(alias="sla", default=None,)
	userCredentialUsageDetails: Optional[list[UserCredentialUsageDetails]] = Field(alias="userCredentialUsageDetails", default=None,)
	userInsights: Optional[UserInsightsRoot] = Field(alias="userInsights", default=None,)

from .app_credential_sign_in_activity import AppCredentialSignInActivity
from .application_sign_in_detailed_summary import ApplicationSignInDetailedSummary
from .authentication_methods_root import AuthenticationMethodsRoot
from .credential_user_registration_details import CredentialUserRegistrationDetails
from .print_usage_by_printer import PrintUsageByPrinter
from .print_usage_by_user import PrintUsageByUser
from .print_usage_by_printer import PrintUsageByPrinter
from .print_usage_by_user import PrintUsageByUser
from .print_usage_by_printer import PrintUsageByPrinter
from .print_usage_by_user import PrintUsageByUser
from .health_monitoring_health_monitoring_root import HealthMonitoringHealthMonitoringRoot
from .print_usage_by_printer import PrintUsageByPrinter
from .print_usage_by_user import PrintUsageByUser
from .print_usage_by_printer import PrintUsageByPrinter
from .print_usage_by_user import PrintUsageByUser
from .partners import Partners
from .security_reports_root import SecurityReportsRoot
from .service_activity import ServiceActivity
from .service_principal_sign_in_activity import ServicePrincipalSignInActivity
from .service_level_agreement_root import ServiceLevelAgreementRoot
from .user_credential_usage_details import UserCredentialUsageDetails
from .user_insights_root import UserInsightsRoot

