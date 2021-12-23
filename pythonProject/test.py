argums = {'AWBS3Bucket':'ct-dev-intelligence-ab/ania-sita-analyzer','DatalakeS3Bucket':'ct-dev-intelligence-datalake' }
lista = ['pcx_vehicle_ait','ab3_07_ania_sita_intermediate_covered_04','pctl_policyperiodstatus','pc_policyperiod','pc_user','pc_credential','pc_policy','pcx_iurcode_ait','pc_job','pc_policyline','pcx_vehiclecov_ait','pctl_mtvehicletype_ait','pc_policycontactrole','pcx_vehiclesubjectrole_ait','pcx_rolesforpolicysubject_ait','pcx_subjectroles_ait','pcx_dailysitanotifications','pctl_genericregistrystauts','ab3_07_ania_sita_intermediate_01','ab3_07_ania_sita_intermediate_02','bc_policyperiod','bc_invoiceitem','bc_invoice','bc_basedistitem','bc_basedist','ab3_07_ania_sita_intermediate_03','bc_basemoneyreceived','bctl_invoiceitemtype','bctl_basemoneyreceived']

def create_entities(entity_list, args):
    """
    Method to build entities dictionary from a list of tables name
    return a dictionary of entities composed

    Parameters
    ----------
        glue_context (glue object): sql context initializated in the init() method 
        entity_list (list): The list for the source table names
        entities_dict (dict): a dictionary empty to be filled with reference to tables

    Returns
    -------
        entities_dict full

    """
    entities_dict = {}

    staging_list = ['ab3_07_ania_sita_intermediate_01', 'ab3_07_ania_sita_intermediate_02',
                    'ab3_07_ania_sita_intermediate_03', 'ab3_07_ania_sita_intermediate_covered_04',
                    'ab3_07_ania_sita_intermediate_covered_05', 'ab3_07_ania_sita_intermediate_covered_06',
                    'ab3_07_ania_sita_intermediate_covered_07', 'ab3_07_ania_sita_intermediate_covered_08',
                    'ab3_07_ania_sita_intermediate_triggers_09', 'ab3_07_ania_sita_intermediate_triggers_10',
                    'ab3_07_ania_sita_intermediate_triggers_11', 'ab3_07_ania_sita_intermediate_triggers_12',
                    'ab3_07_ania_sita_intermediate_triggers_13']

    ania_sita = ['pcx_iurcode_ait', 'pcx_dailysitanotifications', 'pcx_iurcode_ait', 'pctl_genericregistrystauts', ]

    # TODO:check if names are correctly spelled
    for name in entity_list:
        # create a dictionary with the name of the entity to be loaded
        entities_dict[name] = {}
        # Name of the table to be loaded
        entities_dict[name]['source_view_name'] = name
        # read the argument to find the table on: dt_02 if pc /dt_06 if bc/ staging
        if name in staging_list:
            # read from staging destination
            # still to be settled
            entities_dict[name]['database'] = ('{}/df_name=' + name + '/').format(args['AWBS3Bucket'])
        else:
            # read tables from policy center
            if name.startswith("pc") and (name in ania_sita):
                entities_dict[name]['database'] = ('{}/dt2-02-gw-policy-center/ania-sita/df_name=' + name + '/').format(
                    args['DatalakeS3Bucket'])

            elif name.startswith("pc"):
                entities_dict[name]['database'] = ('{}/dt2-02-gw-policy-center/df_name=' + name + '/').format(
                    args['DatalakeS3Bucket'])

            else:
                # tables from billing center
                entities_dict[name]['database'] = ('{}/dt2-06-gw-billing-center/ania-sita/df_name=' + name + '/').format(
                    args['DatalakeS3Bucket'])

    return entities_dict

res = create_entities(lista,argums)

for entity in res:
    print(f'Reading {entity} data from {res[entity]["database"]} ')

entities_to_delete = [a for a in res.keys() if a.endswith(('covered_04'))]
print(entities_to_delete)

for ent in entities_to_delete:
    print(res[ent]['database'])