"""
A Skeleton EDMC Plugin
"""
import sys
import Tkinter as tk


def plugin_start():
    """
    Start this plugin
    :return:
    """
    sys.stderr.write("example plugin started\n")	# appears in %TMP%/EDMarketConnector.log in packaged Windows app


def plugin_prefs(parent):
    """
    Return a TK Frame for adding to the EDMC settings dialog.
    """
    prefs = tk.Frame(parent)
    prefs.columnconfigure(1, weight=1)
    prefs.rowconfigure(4, weight=1)

    tk.Label(prefs, text="Elite Dangerous Market Connector").grid(row=0, column=0, sticky=tk.W)
    tk.Label(prefs, text="Fly Safe!").grid(row=2, column=0, sticky=tk.W)

    if cmdr_data.last is not None:
        datalen = len(str(cmdr_data.last))
        tk.Label(prefs, text="FD sent {} chars".format(datalen)).grid(row=3, column=0, sticky=tk.W)

    return prefs


def plugin_app(parent):
    """
    Return a TK Widget for adding to the EDMC main window.
    :param parent:
    :return:
    """
    return tk.Label(parent, text="---")


def system_changed(timestamp, system):
    """
    Arrived in a new System
    :param timestamp: when we arrived
    :param system: the name of the system
    :return:
    """
    sys.stderr.write("Arrived at {}\n".format(system))


def cmdr_data(data):
    """
    Obtained new data from Frontier about our commander, location and ships
    :param data:
    :return:
    """
    cmdr_data.last = data
    sys.stderr.write("Got new data ({} chars)\n".format(len(str(data))))

cmdr_data.last = None
