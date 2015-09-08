class dclass_parcels(object):
    def __init__(self, id_cntr):
        # area in sqm # pl3 : parcel level 3e
        self.id_cntr                   = id_cntr
        self.parcel_type               = [] # row or tax
        self.muni_id                   = []
        self.land_use_dtax_1           = [] #
        self.land_use_dtax_2           = [] #
        self.land_use                  = [] # 
        self.devarea_lu05              = []
        self.devarea_pl3e              = []
        self.prc_imperviuos            = []
        self.lot_area_sqm_pl3e         = []
        self.lot_area_sqm_lu05         = []
        self.prc_dev_lu05              = [] #100 * self.devarea_lu05 / self.lot_area_sqm_lu05
        self.prc_dev_pl3e              = [] #100 * self.devarea_pl3e / self.lot_area_sqm_pl3e
        self.redevelopment_status      = []
        self.real_estate_type          = []
        self.residential               = []
        self.residential_type          = []
        self.parking                   = []
        self.prc_res_lu05              = []
        self.far                       = []
        self.census_block_2010         = []
        self.census_block_2000         = []
        self.res_infogroup_ids         = []
        self.emp_infogroup_ids         = []
        self.grid250_id_prp_pairs      = []
        self.if_standard_code          = []
        self.tax_rate                  = -0.9999
        self.fy                        = -0.9999
        self.cpi                       = -0.9999
        self.txrev_pac                 = -0.9999
        self.tax_revenue               = -0.9999
        self.txrvpac_13adj             = -0.9999
        self.txrvpac_adj               = -0.9999
        self.totval_pac                = -0.9999
        

    #print "counter=", self.id_cntr
    
    def standard_use_code(self, lookup_dict):

        
        muni_id_key = str(self.muni_id)
        luc_key = str(self.land_use_dtax_1)
        try:
            self.land_use = lookup_dict[(muni_id_key, luc_key)]
        except:
            pass
        
    def det_real_estate_type(self, lookup_dict):
        i_use_code = str(self.land_use_dtax_1)
        _use_code = '"' + i_use_code + '"'
        _far = self.far
        try:
            _real_estate_type = lookup_dict[_use_code]
            if _real_estate_type == '3' and _far >= 0.75:
                self.real_estate_type = '4'
            else:
                self.real_estate_type = _real_estate_type

        except:
            self.real_estate_type = ''
            pass
            
    def det_if_standard_use_code(self, lookup_dict):
        i_use_code = str(self.land_use_dtax_1)
        try:
            _standard_or_not = lookup_dict[i_use_code]
            self.if_standard_code = _standard_or_not
        except:
            self.if_standard_code = 0
            
        
    def gettaxrate(self, txdict, txdictComm, txdictIndus, txdictOpenS):
        i_use_code = str(self.land_use_dtax_1)
        _use_code = '"' + i_use_code + '"'
        print i_use_code
        if i_use_code == None or i_use_code == [] or i_use_code == '':
            pass
        elif i_use_code[0] == '3':
            try:
                txrate = txdictComm[(self.muni_id, self.fy)]
                self.tax_rate = txrate
            except:
                pass
        elif i_use_code[0] == '2':
            try:
                txrate = txdictOpenS[(self.muni_id, self.fy)]
                self.tax_rate = txrate
            except:
                pass
        elif i_use_code[:1] == '01':
            try:
                txrate = txdict[(self.muni_id, self.fy)]
                self.tax_rate = txrate
            except:
                pass
        elif i_use_code[:1] == '03':
            try:
                txrate = txdictComm[(self.muni_id, self.fy)]
                self.tax_rate = txrate
            except:
                pass
        elif i_use_code == '995' and self.muni_id == 35:
            try:
                txrate = txdict[(self.muni_id, self.fy)]
                self.tax_rate = txrate
            except:
                pass
        elif i_use_code[0] == '9':
            self.tax_rate = 0
        elif i_use_code[0] == '4':
            try:
                txrate = txdictIndus[(self.muni_id, self.fy)]
                self.tax_rate = txrate
            except:
                pass
        else:
            try:
                txrate = txdict[(self.muni_id, self.fy)]
                self.tax_rate = txrate
            except:
                pass

    def gettaxrateByMuniName(self, txdict, txdictComm, txdictIndus, txdictOpenS):
        i_use_code = str(self.land_use_dtax_1)
        _use_code = '"' + i_use_code + '"'
        print i_use_code
        if i_use_code == None or i_use_code == [] or i_use_code == '':
            pass
        elif i_use_code[0] == '3':
            try:
                txrate = txdictComm[(self.muni, self.fy)]
                self.tax_rate = txrate
            except:
                pass
        elif i_use_code[0] == '2':
            try:
                txrate = txdictOpenS[(self.muni, self.fy)]
                self.tax_rate = txrate
            except:
                pass
        elif i_use_code[:1] == '01':
            try:
                txrate = txdict[(self.muni, self.fy)]
                self.tax_rate = txrate
            except:
                pass
        elif i_use_code[:1] == '03':
            try:
                txrate = txdictComm[(self.muni, self.fy)]
                self.tax_rate = txrate
            except:
                pass
        elif i_use_code == '995' and self.muni == 35:
            try:
                txrate = txdict[(self.muni, self.fy)]
                self.tax_rate = txrate
            except:
                pass
        elif i_use_code[0] == '9':
            self.tax_rate = 0
        elif i_use_code[0] == '4':
            try:
                txrate = txdictIndus[(self.muni, self.fy)]
                self.tax_rate = txrate
            except:
                pass
        else:
            try:
                txrate = txdict[(self.muni, self.fy)]
                self.tax_rate = txrate
            except:
                pass
    
    def taxRetPerAcre(self):
        if self.tax_rate == None or self.totval_pac == None:
            self.self.txrev_pac = -0.9999
        else:
            txRperAcre = ( self.tax_rate * self.totval_pac )/ 1000
            self.txrev_pac = int(txRperAcre)

    # cpi is coming from Consumer Price Index - All Urban Consumers - Area:  U.S, city average - Item: All items - Base Period: 1982-84 = 100
    def getcpi13(self):
        if self.fy == 2003:
            self.cpi = 184
        elif self.fy == 2004:
            self.cpi = 188.9
        elif self.fy == 2005:
            self.cpi = 195.3
        elif self.fy == 2006:
            self.cpi = 201.6
        elif self.fy == 2007:
            self.cpi = 207.342
        elif self.fy == 2008:
            self.cpi = 215.303
        elif self.fy == 2009:
            self.cpi = 214.537
        elif self.fy == 2010:
            self.cpi = 218.056
        elif self.fy == 2011:
            self.cpi = 224.939
        elif self.fy == 2012:
            self.cpi = 229.594
        elif self.fy == 2013:
            self.cpi = 232.957
        elif self.fy == 2014:
            self.cpi = 236.384

    def getcpi(self, yr):
        if yr == 2003:
            cpi = 184
        elif yr == 2004:
            cpi = 188.9
        elif yr == 2005:
            cpi = 195.3
        elif yr == 2006:
            cpi = 201.6
        elif yr == 2007:
            cpi = 207.342
        elif yr == 2008:
            cpi = 215.303
        elif yr == 2009:
            cpi = 214.537
        elif yr == 2010:
            cpi = 218.056
        elif yr == 2011:
            cpi = 224.939
        elif yr == 2012:
            cpi = 229.594
        elif yr == 2013:
            cpi = 232.957
        elif yr == 2014:
            cpi = 236.384
        return cpi

    def adjustForInflation(self, base_yr_value, target_yr):
        adj_yr_value = base_yr_value * getcpi(self, target_yr) / self.cpi 
        self.taxRetPacAdj = adj_yr_value
    
    def taxRetPerAcre(self):
        if self.totval_pac == None or self.totval_pac == []:
            self.txrev_pac = -0.9999
        else:
            self.txrev_pac = int(( float(self.tax_rate) * self.totval_pac)/ 1000)

    def taxRetPac13Adj(self):
        self.txrvpac_13adj = self.txrev_pac * 232.9367 / self.cpi

    def det_res(self):
        use_code_string = self.land_use_dtax_1
        if use_code_string[:2] in ['10', '11', '12', '14']:
            self.residential = 1
        else:
            self.residential = 0
                
                
    def det_parking(self):
        _use_code = self.standard_use_code
        if (_use_code == 336) or (_use_code == 337):
            self.parking = 1
        else:
            self.parking = 0
            
            
    def det_res_type(self):
        use_code_string = self.land_use_dtax_1
        if use_code_string == ['101']:
            self.residential_type = ['single family']
        elif use_code_string == ['102']:
            self.residential_type = ['condominium']
        elif use_code_string == ['103']:
            self.residential_type = ['mobile homes']    
        elif use_code_string in ['104', '105']:
            self.residential_type = ['multi family']
        elif use_code_string in ['106', '109']:
            self.residential_type = ['improvements']
        elif use_code_string in ['111', '112']:
            self.residential_type = ['apartments']
        elif use_code_string in ['130', '131', '132']:
            self.residential_type = ['vacant']

