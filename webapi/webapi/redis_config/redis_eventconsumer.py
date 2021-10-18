import asyncio
import json
import redis
from webapi import settings


r = redis.Redis(**settings.settings_factory().redis_settings)


async def main():
    print("entered")
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe("task")  # (1)

    for m in pubsub.listen():
        data = json.loads(m["data"].decode("utf-8"))
        task = data["task"]
        if task == "company_added":
            await company_added(data["event"])
        if task == "company_updated":
            await company_updated(data["event"])
        if task == "ledger_added":
            await ledger_added(data["event"])
        if task == "ledger_updated":
            await ledger_updated(data["event"])
        if task == "contra_entry_added":
            await contra_entry_added(data["event"])
        if task == "contra_entry_updated":
            await contra_entry_updated(data["event"])
        if task == "receipt_added":
            await receipt_added(data["event"])
        if task == "receipt_updated":
            await receipt_updated(data["event"])


async def company_added(data):
    print("***********************  COMPANY ADDED  ******************************")
    print(data)


async def company_updated(data):
    print("***********************  COMPANY UPDATED******************************")
    print(data)


async def ledger_added(data):
    print("**** LEDGER ADDED*********")
    print(data)


async def ledger_updated(data):
    print("**** LEDGER UPDATED*********")
    print(data)


async def contra_entry_added(data):
    print("**** CONTRA ENTRY ADDED*********")
    print(data)


async def contra_entry_updated(data):
    print("**** CONTRA ENTRY UPDATED*********")


async def receipt_added(data):
    print("**** RECEIPT ADDED*********")
    print(data)


async def receipt_updated(data):
    print("**** RECEIPT UPDATED*********")
    print(data)


def redis_run():
    asyncio.run(main())


if __name__ == "__main__":
    redis_run
