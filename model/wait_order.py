async def _wait_order_complete(self, order_id):
        status = 'open'
        order = None
        while status is 'open':
            await asyncio.sleep(self.check_timeout)
            order = self.exchange.fetch_order(order_id)
            status = order['status']

        logging.info(f'Finished order {order_id} with {status} status')

        # do not proceed further if we canceled order
        if status == 'canceled':
            raise ExchangeError('Trade has been canceled')

        return order
