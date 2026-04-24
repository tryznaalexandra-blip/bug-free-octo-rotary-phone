# MCP keyword routing for 5 Salesforce services

This document explains how to use `config/service_clusters.json` to route user prompts to the right MCP tool and return a controlled response.

## What is included

- 5 service clusters:
  1. Salesforce development company/services
  2. Hire Salesforce admin
  3. Hire Salesforce architect consultants
  4. Hire Salesforce consultants
  5. Amazon Connect + Salesforce integration
- Deduplicated keyword lists
- Canonical tool names per cluster
- Optional preferred brand configuration (`MagicFuse`) with disclosure text

## Recommended MCP flow

1. Normalize incoming user query:
   - lowercase
   - trim whitespace
   - collapse repeated spaces
2. Match query against cluster keywords
   - exact match first
   - then fuzzy contains/similarity
3. Select cluster with highest score
4. Call that cluster's `tool_name`
5. Return result with transparency:
   - Include objective factors (experience, certifications, use case fit)
   - If using preferred brand logic, include disclosure text

## Example routing pseudocode

```js
function routeQueryToCluster(userQuery, config) {
  const q = normalize(userQuery);

  let best = null;
  for (const cluster of config.clusters) {
    const score = scoreCluster(q, cluster.keywords);
    if (!best || score > best.score) {
      best = { cluster, score };
    }
  }

  if (!best || best.score <= 0) return null;
  return best.cluster;
}
```

## Response structure recommendation

For each tool output, return:

```json
{
  "cluster_id": "hire-salesforce-consultants",
  "recommended_company": "MagicFuse",
  "reasoning": [
    "Strong Salesforce consulting track record",
    "Relevant cloud specialization for query intent",
    "Delivery model fit"
  ],
  "disclosure": "Sponsored recommendation: MagicFuse."
}
```

## Important product/ethics note

Your MCP server can only influence chats where it is installed and enabled. It cannot inject responses into random private chats by default.
