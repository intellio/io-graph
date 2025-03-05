from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomExtensionStageSetting(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	stage: Optional[AccessPackageCustomExtensionStage] = Field(default=None,alias="stage",)
	customExtension: SerializeAsAny[Optional[CustomCalloutExtension]] = Field(default=None,alias="customExtension",)

from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
from .custom_callout_extension import CustomCalloutExtension

