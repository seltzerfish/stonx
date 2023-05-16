from sourcing_strats.tradeview import TopMovers, MostVolatile
from buying_strats.dumb import RandomBuy, ChooseFirst
from selling_strats.trailing_stop import TrailingStop
from selling_strats.dont_sell import DontSellTilEOD, NeverSell, DontSellTilNextDay
from sourcing_strats.hardcoded import Hardcoded
from sourcing_strats.apewisdom import ShortSqueeze
from sourcing_strats.levelfields import LatestBullish
from buying_strats.reddit import Reddit
from strategy import Strategy


TEST_STRATEGY = Strategy(
    "TEST",
    [
        Hardcoded(),
    ],
    ChooseFirst(),
    NeverSell(),
)

LEVELFIELDS_STRATEGY = Strategy(
    "LEVELFIELDS",
    [
        LatestBullish(),
    ],
    ChooseFirst(),
    DontSellTilEOD(),
)

LEVELFIELDS_STRATEGY_ALT = Strategy(
    "LEVELFIELDS",
    [
        LatestBullish(),
    ],
    ChooseFirst(),
    DontSellTilNextDay(),
)