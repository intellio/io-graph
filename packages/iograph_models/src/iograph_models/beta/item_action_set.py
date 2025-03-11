from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ItemActionSet(BaseModel):
	comment: Optional[CommentAction] = Field(alias="comment",default=None,)
	create: Optional[CreateAction] = Field(alias="create",default=None,)
	delete: Optional[DeleteAction] = Field(alias="delete",default=None,)
	edit: Optional[EditAction] = Field(alias="edit",default=None,)
	mention: Optional[MentionAction] = Field(alias="mention",default=None,)
	move: Optional[MoveAction] = Field(alias="move",default=None,)
	rename: Optional[RenameAction] = Field(alias="rename",default=None,)
	restore: Optional[RestoreAction] = Field(alias="restore",default=None,)
	share: Optional[ShareAction] = Field(alias="share",default=None,)
	version: Optional[VersionAction] = Field(alias="version",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .comment_action import CommentAction
from .create_action import CreateAction
from .delete_action import DeleteAction
from .edit_action import EditAction
from .mention_action import MentionAction
from .move_action import MoveAction
from .rename_action import RenameAction
from .restore_action import RestoreAction
from .share_action import ShareAction
from .version_action import VersionAction

