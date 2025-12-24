# KM-F Series Home Assistant Integration

A custom Home Assistant integration for monitoring **KM-F Series** battery management and power systems.

## Overview

This integration provides real-time monitoring of KM-F Series devices through Home Assistant. Track critical battery metrics including charge levels, voltage, current draw, and system status—all accessible from your Home Assistant dashboard.

### 🔋 Supported Sensors

- **Ah Remaining** - Available ampere-hours in the battery
- **Current** - Real-time current draw (positive/negative values)
- **SOC (State of Charge)** - Battery percentage (0-100%)
- **Status** - System state (Charging/Discharging/Idle)
- **Total Capacity** - Maximum battery capacity in Ah
- **Voltage** - System voltage (V)

## Dashboard Preview

The integration displays all sensors in a convenient card view on your Home Assistant dashboard:

![KM-F Series Sensors](https://raw.githubusercontent.com/pexicele/hass-kmf-series/main/assets/km-f-sensors.jpg)

## Installation

### Via HACS (Recommended)

1. Open Home Assistant → **HACS** → **Integrations**
2. Click **⋮** (top right) → **Custom repositories**
3. Add repository URL: `https://github.com/pexicele/hass-kmf-series`
4. Select category: **Integration**
5. Click **Add**
6. Search for **"KM-F Series"** → **Download**
7. **Restart** Home Assistant
8. Go to **Settings** → **Devices & Services** → **+ Create Integration**
9. Select **KM-F Series** and configure

### Manual Installation

1. Clone this repository
2. Copy `custom_components/kmf_series/` to your Home Assistant `custom_components/` directory
3. Restart Home Assistant
4. Add integration via UI

## Configuration

When setting up the integration, you'll need to provide:

- **Device Name** - Display name for the device
- **Host** - IP address or hostname of the KM-F Series device
- **Port** - Communication port (default: 8080)

### Options

After installation, configure polling interval:

- **Scan Interval** - Update frequency in seconds (default: 30s)

## Features

✅ Real-time battery status monitoring  
✅ Multiple sensor types for comprehensive data  
✅ Automatic discovery and polling  
✅ Customizable update intervals  
✅ Dashboard-ready cards  
✅ One-click updates via HACS  

## Automations & Use Cases

Create automations based on KM-F Series sensors:

```yaml
automation:
  - alias: "Alert when battery low"
    trigger:
      platform: numeric_state
      entity_id: sensor.kmf_series_soc
      below: 20
    action:
      service: notify.mobile_app
      data:
        message: "Battery SOC below 20%!"
```

## Troubleshooting

**Integration not appearing?**
- Restart Home Assistant after installation
- Clear browser cache (Ctrl+Shift+Delete)

**No sensor data?**
- Verify device IP/hostname is correct
- Check device is powered and connected
- Review Home Assistant logs for errors

**Need more details?**
- Check Home Assistant logs: Settings → System → Logs

## Support & Contributing

For issues, feature requests, or contributions, please open an issue on GitHub.

## License

MIT License - See LICENSE file for details

---

**Last Updated:** December 2025  
**Version:** 1.0.0  
**Author:** [@pexicele](https://github.com/pexicele)
