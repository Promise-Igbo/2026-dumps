Summary of conversions and deployment guidance

1) Prometheus-native alerting rules
- File: ceph-prometheus-rules.yaml
- Use with a Prometheus server (in-cluster or managed) that accepts Prometheus rule files.
- Apply by adding the file to your Prometheus `rule_files` config or via your Prometheus Operator (create a `PrometheusRule` CRD that references these rules).

2) Grafana alert definitions
- File: grafana-alerts.json
- This is a JSON payload representing Grafana unified alert rules. Replace `__your_prometheus_datasource_uid__` with your Grafana Prometheus datasource UID.
- Create rules via Grafana HTTP API (POST to `/api/ruler-groups/{orgId}/rules` or via provisioning if supported).

3) Azure Managed Prometheus (AMP) guidance
- AMP accepts Prometheus metrics; to enable alerting in Azure-managed flow you can:
  - Import Prometheus alerting rules (Prometheus native YAML) into your AMP workspace if supported by the portal/CLI, or
  - Use AMP's Alertmanager integration (forward alerts to an Alertmanager or Azure Monitor) depending on your configuration.
- If direct import is not supported, use Azure Monitor's alerting by wiring Alertmanager alerts to Azure (webhook) or recreate equivalent alerts in Azure Monitor using the same PromQL (if AMP/portal supports it) or an equivalent metric/log query.

Notes and checks
- Ensure the Prometheus target exposes `ceph_cluster_total_used_bytes` and `ceph_cluster_total_bytes` and that your datasource scrapes them.
- Verify expressions in Prometheus/Grafana show correct values before enabling long retention or notifications.

If you want, I can:
- Create a `PrometheusRule` CRD that wraps `ceph-prometheus-rules.yaml` for use with Prometheus Operator.
- Generate exact Grafana API `curl` commands for importing `grafana-alerts.json` (you'll need Grafana URL + API key).
- Attempt a specific AMP import command if you tell me which Azure CLI or portal workflow you prefer.
