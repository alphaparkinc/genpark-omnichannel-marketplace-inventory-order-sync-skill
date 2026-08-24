class OmnichannelMarketplaceInventoryOrderSyncClient:
    def synchronize_channels(self, central_sku='ID_BATIK_SHIRT_L', updated_stock=45):
        channels = ['Shopee', 'Tokopedia', 'TikTok Shop', 'Lazada', 'Shopify Brand Store']
        return {
            'sync_batch_id': 'srcl_sync_10294',
            'sku': central_sku,
            'broadcast_stock_level': updated_stock,
            'synchronized_channels_count': len(channels),
            'active_channels': channels,
            'sync_latency_ms': 310,
            'oversell_prevention_lock_acquired': True
        }
