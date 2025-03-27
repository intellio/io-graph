from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class SingleSignOnExtension(BaseModel):
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
			if mapping_key == "#microsoft.graph.credentialSingleSignOnExtension":
				from .credential_single_sign_on_extension import CredentialSingleSignOnExtension
				return CredentialSingleSignOnExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.iosSingleSignOnExtension":
				from .ios_single_sign_on_extension import IosSingleSignOnExtension
				return IosSingleSignOnExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.iosAzureAdSingleSignOnExtension":
				from .ios_azure_ad_single_sign_on_extension import IosAzureAdSingleSignOnExtension
				return IosAzureAdSingleSignOnExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.iosCredentialSingleSignOnExtension":
				from .ios_credential_single_sign_on_extension import IosCredentialSingleSignOnExtension
				return IosCredentialSingleSignOnExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.iosKerberosSingleSignOnExtension":
				from .ios_kerberos_single_sign_on_extension import IosKerberosSingleSignOnExtension
				return IosKerberosSingleSignOnExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.iosRedirectSingleSignOnExtension":
				from .ios_redirect_single_sign_on_extension import IosRedirectSingleSignOnExtension
				return IosRedirectSingleSignOnExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.kerberosSingleSignOnExtension":
				from .kerberos_single_sign_on_extension import KerberosSingleSignOnExtension
				return KerberosSingleSignOnExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSSingleSignOnExtension":
				from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension
				return MacOSSingleSignOnExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSAzureAdSingleSignOnExtension":
				from .mac_o_s_azure_ad_single_sign_on_extension import MacOSAzureAdSingleSignOnExtension
				return MacOSAzureAdSingleSignOnExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSCredentialSingleSignOnExtension":
				from .mac_o_s_credential_single_sign_on_extension import MacOSCredentialSingleSignOnExtension
				return MacOSCredentialSingleSignOnExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSKerberosSingleSignOnExtension":
				from .mac_o_s_kerberos_single_sign_on_extension import MacOSKerberosSingleSignOnExtension
				return MacOSKerberosSingleSignOnExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSRedirectSingleSignOnExtension":
				from .mac_o_s_redirect_single_sign_on_extension import MacOSRedirectSingleSignOnExtension
				return MacOSRedirectSingleSignOnExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.redirectSingleSignOnExtension":
				from .redirect_single_sign_on_extension import RedirectSingleSignOnExtension
				return RedirectSingleSignOnExtension.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


