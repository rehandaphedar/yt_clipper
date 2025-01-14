import logging
from pathlib import Path

import coloredlogs
import verboselogs

from clipper.clipper_types import ClipperState

# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0


class YTCLogger(verboselogs.VerboseLogger):
    def important(self, msg: str, *args, **kwargs) -> None:  # noqa: ANN002, ANN003
        self.log(29, msg, *args, **kwargs)

    def notice(self, msg: str, *args, **kwargs) -> None:  # noqa: ANN002, ANN003
        self.log(32, msg, *args, **kwargs)

    def header(self, msg: str, *args, **kwargs) -> None:  # noqa: ANN002, ANN003
        self.log(33, msg, *args, **kwargs)

    def report(self, msg: str, *args, **kwargs) -> None:  # noqa: ANN002, ANN003
        self.log(34, msg, *args, **kwargs)


logger = YTCLogger(__name__)


def setUpLogger(cs: ClipperState) -> None:
    settings = cs.settings
    cp = cs.clipper_paths

    verboselogs.add_log_level(29, "IMPORTANT")
    verboselogs.add_log_level(32, "NOTICE")
    verboselogs.add_log_level(33, "HEADER")
    verboselogs.add_log_level(34, "REPORT")

    formatString = r"[%(asctime)s] (ln %(lineno)d) %(levelname)s: %(message)s"
    coloredlogs.DEFAULT_LOG_FORMAT = formatString
    coloredlogs.DEFAULT_FIELD_STYLES["levelname"] = {"color": "white"}
    coloredlogs.DEFAULT_LEVEL_STYLES["DEBUG"] = {"color": 219}  # pink # type: ignore
    coloredlogs.DEFAULT_LEVEL_STYLES["IMPORTANT"] = {"color": 209}  # orange  # type: ignore
    coloredlogs.DEFAULT_LEVEL_STYLES["NOTICE"] = {"color": "magenta"}
    coloredlogs.DEFAULT_LEVEL_STYLES["HEADER"] = {"color": "blue"}
    coloredlogs.DEFAULT_LEVEL_STYLES["REPORT"] = {"color": "cyan"}

    datefmt = "%y-%m-%d %H:%M:%S"
    log_level = settings.get("logLevel") or verboselogs.VERBOSE
    coloredlogs.install(level=log_level, datefmt=datefmt)

    coloredFormatter = coloredlogs.ColoredFormatter(datefmt=datefmt)

    reportHandler = logging.StreamHandler(cs.reportStream)
    reportHandler.setLevel(32)
    logger.addHandler(reportHandler)
    reportHandlerColored = logging.StreamHandler(cs.reportStreamColored)
    reportHandlerColored.setLevel(32)
    reportHandlerColored.setFormatter(coloredFormatter)
    logger.addHandler(reportHandlerColored)

    if not settings["preview"]:
        cp.logFilePath = f'{cp.clipsPath}/{settings["titleSuffix"]}.log'
        fileHandler = logging.FileHandler(
            filename=cp.logFilePath,
            mode="a",
            encoding="utf-8",
        )
        formatter = coloredlogs.BasicFormatter(datefmt=datefmt)
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)


def printReport(cs: ClipperState) -> None:
    cp = cs.clipper_paths

    reportColored = cs.reportStreamColored.getvalue()
    logger.info("-" * 80)
    logger.header("#" * 30 + " Summary Report " + "#" * 30)
    print(reportColored)

    if Path(cp.logFilePath).is_file():
        report = cs.reportStream.getvalue()
        with open(cp.logFilePath, "a", encoding="utf-8") as f:
            f.write(report)
