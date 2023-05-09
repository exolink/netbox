from django.utils.translation import gettext as _

from netbox.registry import registry
from . import *

#
# Nav menus
#

ORGANIZATION_MENU = Menu(
    label=_('Organisation'),
    icon_class='mdi mdi-domain',
    groups=(
        MenuGroup(
            label=_('Standorte'),
            items=(
                get_model_item('dcim', 'site', _('Standorte')),
                get_model_item('dcim', 'region', _('Regionen')),
                get_model_item('dcim', 'sitegroup', _('Standortgruppen')),
                get_model_item('dcim', 'location', _('Standort-Unterteilungen')),
            ),
        ),
        # MenuGroup(
        #     label=_('Tenancy'),
        #     items=(
        #         get_model_item('tenancy', 'tenant', _('Tenants')),
        #         get_model_item('tenancy', 'tenantgroup', _('Tenant Groups')),
        #     ),
        # ),
        # MenuGroup(
        #     label=_('Contacts'),
        #     items=(
        #         get_model_item('tenancy', 'contact', _('Contacts')),
        #         get_model_item('tenancy', 'contactgroup', _('Contact Groups')),
        #         get_model_item('tenancy', 'contactrole', _('Contact Roles')),
        #         get_model_item('tenancy', 'contactassignment', _('Contact Assignments'), actions=[]),
        #     ),
        # ),
    ),
)

DEVICES_MENU = Menu(
    label=_('Geräte'),
    icon_class='mdi mdi-server',
    groups=(
        MenuGroup(
            label=_('Ladesäulen'),
            items=(
                get_model_item('dcim', 'device', _('Ladesäulen')),
                get_model_item('dcim', 'module', _('Module')),
                get_model_item('dcim', 'devicerole', _('Ladesäulen-Arten')),
            ),
        ),
        MenuGroup(
            label=_('Device Types'),
            items=(
                get_model_item('dcim', 'devicetype', _('Modelle')),
                get_model_item('dcim', 'moduletype', _('Modultypen')),
                get_model_item('dcim', 'manufacturer', _('Hersteller')),
            ),
        ),
        MenuGroup(
            label=_('Komponenten'),
            items=(
#                get_model_item('dcim', 'interface', _('Interfaces')),
#                get_model_item('dcim', 'frontport', _('Front Ports')),
#                get_model_item('dcim', 'rearport', _('Rear Ports')),
#                get_model_item('dcim', 'powerport', _('Power Ports')),
                get_model_item('dcim', 'poweroutlet', _('Ladepunkte')),
#                get_model_item('dcim', 'modulebay', _('Module Bays')),
#                get_model_item('dcim', 'devicebay', _('Device Bays')),
                get_model_item('dcim', 'inventoryitem', _('SIM-Karten')),
#                get_model_item('dcim', 'inventoryitemrole', _('Inventory Item Roles')),
            ),
        ),
    ),
)

# CONNECTIONS_MENU = Menu(
#     label=_('Connections'),
#     icon_class='mdi mdi-connection',
#     groups=(
#         MenuGroup(
#             label=_('Connections'),
#             items=(
#                 get_model_item('dcim', 'cable', _('Cables'), actions=['import']),
#                 get_model_item('wireless', 'wirelesslink', _('Wireless Links'), actions=['import']),
#                 MenuItem(
#                     link='dcim:interface_connections_list',
#                     link_text=_('Interface Connections'),
#                     permissions=['dcim.view_interface']
#                 ),
#                 MenuItem(
#                     link='dcim:console_connections_list',
#                     link_text=_('Console Connections'),
#                     permissions=['dcim.view_consoleport']
#                 ),
#                 MenuItem(
#                     link='dcim:power_connections_list',
#                     link_text=_('Power Connections'),
#                     permissions=['dcim.view_powerport']
#                 ),
#             ),
#         ),
#     ),
# )

# WIRELESS_MENU = Menu(
#     label=_('Wireless'),
#     icon_class='mdi mdi-wifi',
#     groups=(
#         MenuGroup(
#             label=_('Wireless'),
#             items=(
#                 get_model_item('wireless', 'wirelesslan', _('Wireless LANs')),
#                 get_model_item('wireless', 'wirelesslangroup', _('Wireless LAN Groups')),
#             ),
#         ),
#     ),
# )

# IPAM_MENU = Menu(
#     label=_('IPAM'),
#     icon_class='mdi mdi-counter',
#     groups=(
#         MenuGroup(
#             label=_('IP Addresses'),
#             items=(
#                 get_model_item('ipam', 'ipaddress', _('IP Addresses')),
#                 get_model_item('ipam', 'iprange', _('IP Ranges')),
#             ),
#         ),
#         MenuGroup(
#             label=_('Prefixes'),
#             items=(
#                 get_model_item('ipam', 'prefix', _('Prefixes')),
#                 get_model_item('ipam', 'role', _('Prefix & VLAN Roles')),
#             ),
#         ),
#         MenuGroup(
#             label=_('ASNs'),
#             items=(
#                 get_model_item('ipam', 'asnrange', _('ASN Ranges')),
#                 get_model_item('ipam', 'asn', _('ASNs')),
#             ),
#         ),
#         MenuGroup(
#             label=_('Aggregates'),
#             items=(
#                 get_model_item('ipam', 'aggregate', _('Aggregates')),
#                 get_model_item('ipam', 'rir', _('RIRs')),
#             ),
#         ),
#         MenuGroup(
#             label=_('VRFs'),
#             items=(
#                 get_model_item('ipam', 'vrf', _('VRFs')),
#                 get_model_item('ipam', 'routetarget', _('Route Targets')),
#             ),
#         ),
#         MenuGroup(
#             label=_('VLANs'),
#             items=(
#                 get_model_item('ipam', 'vlan', _('VLANs')),
#                 get_model_item('ipam', 'vlangroup', _('VLAN Groups')),
#             ),
#         ),
#         MenuGroup(
#             label=_('Other'),
#             items=(
#                 get_model_item('ipam', 'fhrpgroup', _('FHRP Groups')),
#                 get_model_item('ipam', 'servicetemplate', _('Service Templates')),
#                 get_model_item('ipam', 'service', _('Services')),
#             ),
#         ),
#     ),
# )

# CIRCUITS_MENU = Menu(
#     label=_('Circuits'),
#     icon_class='mdi mdi-transit-connection-variant',
#     groups=(
#         MenuGroup(
#             label=_('Circuits'),
#             items=(
#                 get_model_item('circuits', 'circuit', _('Circuits')),
#                 get_model_item('circuits', 'circuittype', _('Circuit Types')),
#             ),
#         ),
#         MenuGroup(
#             label=_('Providers'),
#             items=(
#                 get_model_item('circuits', 'provider', _('Providers')),
#                 get_model_item('circuits', 'provideraccount', _('Provider Accounts')),
#                 get_model_item('circuits', 'providernetwork', _('Provider Networks')),
#             ),
#         ),
#     ),
# )

# POWER_MENU = Menu(
#     label=_('Power'),
#     icon_class='mdi mdi-flash',
#     groups=(
#         MenuGroup(
#             label=_('Power'),
#             items=(
#                 get_model_item('dcim', 'powerfeed', _('Power Feeds')),
#                 get_model_item('dcim', 'powerpanel', _('Power Panels')),
#             ),
#         ),
#     ),
# )

# PROVISIONING_MENU = Menu(
#     label=_('Provisioning'),
#     icon_class='mdi mdi-file-document-multiple-outline',
#     groups=(
#         MenuGroup(
#             label=_('Configurations'),
#             items=(
#                 get_model_item('extras', 'configcontext', _('Config Contexts'), actions=['add']),
#                 get_model_item('extras', 'configtemplate', _('Config Templates'), actions=['add']),
#             ),
#         ),
#     ),
# )

CUSTOMIZATION_MENU = Menu(
    label=_('Anpassungen'),
    icon_class='mdi mdi-toolbox-outline',
    groups=(
        MenuGroup(
            label=_('Anpassungen'),
            items=(
                get_model_item('extras', 'customfield', _('Custom Fields')),
                # get_model_item('extras', 'customlink', _('Custom Links')),
                # get_model_item('extras', 'exporttemplate', _('Export Templates')),
                # get_model_item('extras', 'savedfilter', _('Saved Filters')),
                # get_model_item('extras', 'tag', 'Tags'),
            ),
        ),
        # MenuGroup(
        #     label=_('Reports & Scripts'),
        #     items=(
        #         MenuItem(
        #             link='extras:report_list',
        #             link_text=_('Reports'),
        #             permissions=['extras.view_report']
        #         ),
        #         MenuItem(
        #             link='extras:script_list',
        #             link_text=_('Scripts'),
        #             permissions=['extras.view_script']
        #         ),
        #     ),
        # ),
    ),
)

# OPERATIONS_MENU = Menu(
#     label=_('Operations'),
#     icon_class='mdi mdi-cogs',
#     groups=(
#         MenuGroup(
#             label=_('Integrations'),
#             items=(
#                 get_model_item('core', 'datasource', _('Data Sources')),
#                 get_model_item('extras', 'webhook', _('Webhooks')),
#             ),
#         ),
#         MenuGroup(
#             label=_('Jobs'),
#             items=(
#                 MenuItem(
#                     link='core:job_list',
#                     link_text=_('Jobs'),
#                     permissions=['core.view_job'],
#                 ),
#             ),
#         ),
#         MenuGroup(
#             label=_('Logging'),
#             items=(
#                 get_model_item('extras', 'journalentry', _('Journal Entries'), actions=[]),
#                 get_model_item('extras', 'objectchange', _('Change Log'), actions=[]),
#             ),
#         ),
#     ),
# )


MENUS = [
    ORGANIZATION_MENU,
    DEVICES_MENU,
    # CONNECTIONS_MENU,
    # WIRELESS_MENU,
    # IPAM_MENU,
    # CIRCUITS_MENU,
    # POWER_MENU,
    # PROVISIONING_MENU,
    CUSTOMIZATION_MENU,
    # OPERATIONS_MENU,
]

#
# Add plugin menus
#

for menu in registry['plugins']['menus']:
    MENUS.append(menu)

if registry['plugins']['menu_items']:

    # Build the default plugins menu
    groups = [
        MenuGroup(label=label, items=items)
        for label, items in registry['plugins']['menu_items'].items()
    ]
    plugins_menu = Menu(
        label=_("Plugins"),
        icon_class="mdi mdi-puzzle",
        groups=groups
    )
    MENUS.append(plugins_menu)
