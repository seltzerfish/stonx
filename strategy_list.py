from sourcing_strats.tradeview import TopMovers, MostVolatile
from buying_strats.dumb import RandomBuy, ChooseFirst
from selling_strats.trailing_stop import TrailingStop
from selling_strats.dont_sell import DontSellTilEOD, NeverSell
from sourcing_strats.google_news import GoogNewsBest
from strategy import Strategy


TEST_STRATEGY = Strategy(
    "TEST",
    [
        MostVolatile(),
        TopMovers(),
    ],
    RandomBuy(),
    TrailingStop(),
)

GOOG_NEWS_TEST_STRATEGY = Strategy(
    "GOOG_NEWS_TEST",
    [
        GoogNewsBest(),
    ],
    ChooseFirst(),
    DontSellTilEOD(),
)
