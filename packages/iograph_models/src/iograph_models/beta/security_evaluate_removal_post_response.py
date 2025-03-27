from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Security_evaluate_removalPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[SecurityAddContentFooterAction, SecurityAddContentHeaderAction, SecurityAddWatermarkAction, SecurityApplyLabelAction, SecurityCustomAction, SecurityJustifyAction, SecurityMetadataAction, SecurityProtectAdhocAction, SecurityProtectByTemplateAction, SecurityProtectDoNotForwardAction, SecurityRecommendLabelAction, SecurityRemoveContentFooterAction, SecurityRemoveContentHeaderAction, SecurityRemoveProtectionAction, SecurityRemoveWatermarkAction]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .security_add_content_footer_action import SecurityAddContentFooterAction
from .security_add_content_header_action import SecurityAddContentHeaderAction
from .security_add_watermark_action import SecurityAddWatermarkAction
from .security_apply_label_action import SecurityApplyLabelAction
from .security_custom_action import SecurityCustomAction
from .security_justify_action import SecurityJustifyAction
from .security_metadata_action import SecurityMetadataAction
from .security_protect_adhoc_action import SecurityProtectAdhocAction
from .security_protect_by_template_action import SecurityProtectByTemplateAction
from .security_protect_do_not_forward_action import SecurityProtectDoNotForwardAction
from .security_recommend_label_action import SecurityRecommendLabelAction
from .security_remove_content_footer_action import SecurityRemoveContentFooterAction
from .security_remove_content_header_action import SecurityRemoveContentHeaderAction
from .security_remove_protection_action import SecurityRemoveProtectionAction
from .security_remove_watermark_action import SecurityRemoveWatermarkAction

