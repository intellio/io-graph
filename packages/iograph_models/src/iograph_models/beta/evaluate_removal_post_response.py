from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Evaluate_removalPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AddContentFooterAction, AddContentHeaderAction, AddWatermarkAction, ApplyLabelAction, CustomAction, JustifyAction, MetadataAction, ProtectAdhocAction, ProtectByTemplateAction, ProtectDoNotForwardAction, RecommendLabelAction, RemoveContentFooterAction, RemoveContentHeaderAction, RemoveProtectionAction, RemoveWatermarkAction]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .add_content_footer_action import AddContentFooterAction
from .add_content_header_action import AddContentHeaderAction
from .add_watermark_action import AddWatermarkAction
from .apply_label_action import ApplyLabelAction
from .custom_action import CustomAction
from .justify_action import JustifyAction
from .metadata_action import MetadataAction
from .protect_adhoc_action import ProtectAdhocAction
from .protect_by_template_action import ProtectByTemplateAction
from .protect_do_not_forward_action import ProtectDoNotForwardAction
from .recommend_label_action import RecommendLabelAction
from .remove_content_footer_action import RemoveContentFooterAction
from .remove_content_header_action import RemoveContentHeaderAction
from .remove_protection_action import RemoveProtectionAction
from .remove_watermark_action import RemoveWatermarkAction

