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
        
        print "counter=", self.id_cntr
    
    
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
            self.residential_type = 'single family'
        elif use_code_string == ['102']:
            self.residential_type = 'condominium'
        elif use_code_string == ['103']:
            self.residential_type = 'mobile homes'  
        elif use_code_string in ['104', '105']:
            self.residential_type = 'multi family'
        elif use_code_string in ['106', '109']:
            self.residential_type = 'improvements'
        elif use_code_string in ['111', '112']:
            self.residential_type = 'apartments'
        elif use_code_string in ['130', '131', '132']:
            self.residential_type = 'vacant'



# the following class members are all the results of union between cencsus blocka (here 2000) and parcels                                   
class each_parcel_part(dclass_parcels):
    def __init__(self):
        self.block_id = []
        self.part_area = []

        
        
class each_parcel_part_block00(dclass_parcels):
    def __init__(self):
        self.block_id           = []
        self.part_block00_area  = []
        
class each_parcel_part_block10(dclass_parcels):
    def __init__(self):
        self.block_id           = []
        self.part_block10_area  = []
        
        
class each_parcel_part_luc05_blk00_grid25(dclass_parcels):
    def __init__(self):
        self.part_area          = []
        self.luc05_id           = []
        self.luc05_use_code     = []
        self.part_luc05_area    = []
        self.luc05_residential  = []
        self.block_id00         = []
        self.part_block00_area  = []
        self.grid_id            = []
        self.part_grid_area     = []
        
    def det_luc05_residential(self, code):
        use_code = code
        print "inside class use code: ", use_code
        str_use_code = str(use_code)
        if (use_code == 10) or (use_code == 11) or (use_code == 12) or (use_code == 13) or (use_code == 38):
            self.luc05_residential = 1
        else:
            self.luc05_residential = 0