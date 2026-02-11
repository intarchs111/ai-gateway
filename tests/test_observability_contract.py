from src.observability.metrics import record_metrics


def test_metrics_accept_none_usage():
    # Should not raise
    record_metrics(None)
