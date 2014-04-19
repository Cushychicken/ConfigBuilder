import re

def getPNList():
    """
        Builds initial list of Part Numbers for qual build
    """
    pn_re = re.compile(r'\d{3}-\d{5}')
    all_pns = []
    while True:
        print "Qual Build PN List"
        print "=================="
        print '\n'.join(all_pns)
        print
        new_pn = raw_input("Please enter a new part number (or 'done'): ")
        if pn_re.search(new_pn):
            all_pns.append(new_pn)
        elif new_pn.lower() == 'done':
            break
        else:
            print "Sorry, that part number wasn't valid."

    return all_pns
    
def getConfigStatus(all_pns):
    """
        Gets configuration status for all build targets
    """
    pn_build_config = []
    for pn in all_pns:
        configs = raw_input("Will %s have multiple build configs? (y/n - blank is no) :" % pn)
        if configs.lower() == 'y':
            pn_build_config.append([pn, True])
        elif configs.lower() == 'n':
            pn_build_config.append([pn, False])
        elif configs.lower() == '':
            pn_build_config.append([pn, False])
    assert len(pn_build_config) == len(all_pns), "Not all PNs got configured."
    return pn_build_config
    
def getConfigQuantity(build_configs):
    """
        Gets number of configurations 
    """
    config_qtys = []
    for cfg in build_configs:
        print cfg
        if cfg[1]:
            qty = raw_input("Please enter the number of build configurations for %s (default is 1): " % cfg[0])
            cfg.append(qty)
            config_qtys.append(cfg)
        else:
            cfg.append('1')
            config_qtys.append(cfg)
    return config_qtys
    
def getPartData(config_qtys):
    extra_cfgs = {}
    for cfg in config_qtys:
        if cfg[1]:
            i = 0
            cfg_list = []
            while i < cfg[2]:
                print "%s: mfg configuration %d" % (cfg[0], (i+1))
                mfg = raw_input("Please enter the manufacturer of new %s: " % cfg[0])
                mpn = raw_input("Please enter the mfg part no. of new %s: " % cfg[0])
                cfg_list.append([mfg, mpn])
                i += 1
        else:
            mfg = raw_input("Please enter the manufacturer of new %s: " % cfg[0])
            mpn = raw_input("Please enter the mfg part no. of new %s: " % cfg[0])
    
def getConfigCombinations(config_qtys):
    multi_cfg = [ cfg for cfg in config_qtys if cfg[1] ]
    print multi_cfg
            
if __name__ == '__main__':
    all_pns = getPNList()
    configs = getConfigStatus(all_pns)
    cfg_qty = getConfigQuantity(configs)
    cfg_inf = getPartData(cfg_qty)
    
    print 'Final PN List with Statuses and Qunatities'
    print '\n'.join([ cfg[0] + '\t' + str(cfg[1]) + '\t' + str(cfg[2]) for cfg in cfg_qty ])