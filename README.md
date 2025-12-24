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

## Device

![KM-F Series Device](https://i.ebayimg.com/images/g/O-QAAOSwEEdnYmwc/s-l1600.webp)

*KM-F Series battery management system for accurate power monitoring and control*

## Dashboard Preview

The integration displays all sensors in a convenient card view on your Home Assistant dashboard:

| Sensor | Value |
|--------|-------|
| Ah Remaining | 950.453 Ah |
| Current | -4.93 A |
| SOC | 76.0% |
| Status | Discharging |
| Total Capacity | 1,250 Ah |
| Voltage | 51.38 V |

*Screenshot of Home Assistant KM-F Series sensor display*

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
- **Port** - Communication port (default: 8899)

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

  - alias: "Stop charging when full"
    trigger:
      platform: numeric_state
      entity_id: sensor.kmf_series_soc
      above: 95
    action:
      service: switch.turn_off
      entity_id: switch.charger
```

## Troubleshooting

**Integration not appearing?**
- Restart Home Assistant after installation
- Clear browser cache (Ctrl+Shift+Delete)

**No sensor data?**
- Verify device IP/hostname is correct
- Check device is powered and connected
- Ensure port 8899 is accessible
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
