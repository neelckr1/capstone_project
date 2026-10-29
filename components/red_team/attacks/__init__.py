"""Attack generator package initialization."""
from attacks.base_attack import BaseAttack
from attacks.quine_attack import QuineReplicatorAttack
from attacks.crescendo_attack import CrescendoDriftAttack
from attacks.tree_search_attack import TreeSearchAttack
from attacks.delimiter_spoof import DelimiterSpoofAttack

__all__ = [
    "BaseAttack",
    "QuineReplicatorAttack",
    "CrescendoDriftAttack",
    "TreeSearchAttack",
    "DelimiterSpoofAttack",
]
