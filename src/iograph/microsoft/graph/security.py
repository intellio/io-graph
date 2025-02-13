# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-02-13T03:52:51+00:00

from __future__ import annotations

from typing import Literal

from pydantic import Field, RootModel


class BehaviorDuringRetentionPeriod(
    RootModel[
        Literal[
            'doNotRetain',
            'retain',
            'retainAsRecord',
            'retainAsRegulatoryRecord',
            'unknownFutureValue',
        ]
    ]
):
    root: Literal[
        'doNotRetain',
        'retain',
        'retainAsRecord',
        'retainAsRegulatoryRecord',
        'unknownFutureValue',
    ] = Field(..., title='behaviorDuringRetentionPeriod')
