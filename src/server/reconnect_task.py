import asyncio


def start_reconnect_task(server, peer_info, log, auth):
    """
    Start a background task that checks connection and reconnects periodically to a peer.
    """

    async def connection_check():
        while True:
            peer_retry = True

            for connection in server.global_connections.get_connections():
                if connection.get_peer_info() == peer_info:
                    peer_retry = False

            if peer_retry:
                log.info(f"Reconnecting to peer {peer_info}")
                await server.start_client(peer_info, None, auth=auth)
            await asyncio.sleep(3)

    return asyncio.create_task(connection_check())
