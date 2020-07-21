#!/usr/bin/env python3

import matplotlib
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

font = {'weight': 'bold', 'size': 22}

matplotlib.rc('font', **font)


def convert_latency_to_ms(latency):
    """
    Converts wrk output to float
    """
    if "ms" in latency:
        latency = float(latency.replace("ms", ""))
    else:
        latency = float(latency.replace("us", "")) / 1000
    return latency


def convert_reqs_to_float(reqs):
    """
    Converts wrk output to float
    """
    if "k" in reqs:
        reqs = float(reqs.replace("k", "")) * 1000
    else:
        reqs = float(reqs)
    return reqs


def get_stats(filename):
    """
    Retrieves latency, reqs/sec output from wrk with standard deviations
    Output is tuple
    """
    with open(filename) as input_data:
        for line in input_data:
            line = line.strip().split()
            if line[0] == "Latency":
                latency = convert_latency_to_ms(line[1])
                latency_std = convert_latency_to_ms(line[2])
            elif line[0] == "Req/Sec":
                reqs_per_sec = convert_reqs_to_float(line[1])
                reqs_per_sec_std = convert_reqs_to_float(line[2])
    return (latency, latency_std, reqs_per_sec, reqs_per_sec_std)


def gather_data(servers, frameworks, dtype):
    data = []
    for server in servers:
        for framework in frameworks:
            stats = get_stats(f"../{dtype}/{server}_{framework}.log")
            data.append((server, framework, *stats))
    df = pd.DataFrame(data,
                      columns=[
                          f"{dtype}", "framework", "latency", "latency std",
                          "reqs/sec", "reqs/sec std"
                      ])
    return df


def gather_wsgi_data():
    return gather_data(
        ["bjoern", "cherrypy", "gunicorn", "meinheld", "twisted", "uwsgi"],
        ["falcon", "flask"], "wsgi")


def gather_asgi_data():
    return gather_data(["daphne", "hypercorn", "uvicorn"], [
        "blacksheep", "falcon", "fastapi", "molten", "responder", "sanic",
        "starlette"
    ], "asgi")


def plot_data(input_df, dtype):
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(x="framework", y="reqs/sec", hue=dtype, data=input_df, ax=ax)
    plt.legend()
    ax.set_yscale("log")
    plt.savefig(f"{dtype}_request_speed.png")

    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(x="framework", y="latency", hue=dtype, data=input_df, ax=ax)
    plt.legend()
    ax.set_yscale("log")
    ax.set_ylabel("latency (ms)")
    plt.savefig(f"{dtype}_latency.png")


def plot_wsgi_data(wsgi_df):
    plot_data(wsgi_df, "wsgi")


def plot_asgi_data(asgi_df):
    plot_data(asgi_df, "asgi")


def main():
    wsgi_df = gather_wsgi_data()
    plot_wsgi_data(wsgi_df)
    asgi_df = gather_asgi_data()
    plot_asgi_data(asgi_df)


if __name__ == "__main__":
    main()
