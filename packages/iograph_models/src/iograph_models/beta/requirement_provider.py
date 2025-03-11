from __future__ import annotations
from enum import StrEnum


class RequirementProvider(StrEnum):
	user = "user"
	request = "request"
	servicePrincipal = "servicePrincipal"
	v1ConditionalAccess = "v1ConditionalAccess"
	multiConditionalAccess = "multiConditionalAccess"
	tenantSessionRiskPolicy = "tenantSessionRiskPolicy"
	accountCompromisePolicies = "accountCompromisePolicies"
	v1ConditionalAccessDependency = "v1ConditionalAccessDependency"
	v1ConditionalAccessPolicyIdRequested = "v1ConditionalAccessPolicyIdRequested"
	mfaRegistrationRequiredByIdentityProtectionPolicy = "mfaRegistrationRequiredByIdentityProtectionPolicy"
	baselineProtection = "baselineProtection"
	mfaRegistrationRequiredByBaselineProtection = "mfaRegistrationRequiredByBaselineProtection"
	mfaRegistrationRequiredByMultiConditionalAccess = "mfaRegistrationRequiredByMultiConditionalAccess"
	enforcedForCspAdmins = "enforcedForCspAdmins"
	securityDefaults = "securityDefaults"
	mfaRegistrationRequiredBySecurityDefaults = "mfaRegistrationRequiredBySecurityDefaults"
	proofUpCodeRequest = "proofUpCodeRequest"
	crossTenantOutboundRule = "crossTenantOutboundRule"
	gpsLocationCondition = "gpsLocationCondition"
	riskBasedPolicy = "riskBasedPolicy"
	unknownFutureValue = "unknownFutureValue"
	scopeBasedAuthRequirementPolicy = "scopeBasedAuthRequirementPolicy"
	authenticationStrengths = "authenticationStrengths"

