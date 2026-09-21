### Building [Saykai](https://saykai.com)

A safety gate for ROS 2 CI/CD. Blocks or reports on pull requests against a spec, so unsafe robotics code doesn't merge quietly.

The repos below run on the same instinct: catch what's actually happening, whether that's a system, a dataset, or an MCP call, before it causes damage nobody can trace back.

<!-- LATEST:START -->
```
$ git log -1 --oneline --all-repos
1c3a8ab  feat: idle-time analysis with declared per-channel motion thresholds  (mekiki)
```
<!-- LATEST:END -->

### Shipped

- **[saykai-action](https://github.com/saykai-systems/saykai-action)** / **saykai-examples**: the safety gate itself and example integrations, public under [saykai-systems](https://github.com/saykai-systems).
- **[mekiki](https://github.com/bradsward/mekiki)**: finds the bad demonstrations in robot learning datasets before you train on them. action-state mismatches, dead frames, camera desync, coverage gaps. reads real Open X-Embodiment / LeRobot data.
- **[greenlight](https://github.com/bradsward/greenlight)**: transparent proxy and live trace viewer for MCP (Model Context Protocol). stdio and Streamable HTTP, published on PyPI.
- **[hirogari](https://github.com/bradsward/hirogari)**: measures whether an OSS release, doc change, or post actually moved adoption, and whether it stuck. public data only.

### Reach me

[saykai.com](https://saykai.com) · [x.com/bradward](https://x.com/bradward)
