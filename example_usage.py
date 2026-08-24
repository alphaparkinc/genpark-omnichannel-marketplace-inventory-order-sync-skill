from client import OmnichannelMarketplaceInventoryOrderSyncClient

def main():
    client = OmnichannelMarketplaceInventoryOrderSyncClient()
    res = client.synchronize_channels('ID_COFFEE_DRIP_BOX', 120)
    print('Sync Batch: ' + res['sync_batch_id'] + ' | Stock: ' + str(res['broadcast_stock_level']))
    print('Channels (' + str(res['synchronized_channels_count']) + '): ' + ', '.join(res['active_channels']))
    print('Latency: ' + str(res['sync_latency_ms']) + 'ms | Oversell Lock: ' + str(res['oversell_prevention_lock_acquired']))

if __name__ == '__main__':
    main()
