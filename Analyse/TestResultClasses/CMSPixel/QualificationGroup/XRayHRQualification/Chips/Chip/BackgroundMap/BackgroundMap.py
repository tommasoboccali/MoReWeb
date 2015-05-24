# -*- coding: utf-8 -*-
import ROOT
import AbstractClasses
import AbstractClasses.Helper.HistoGetter as HistoGetter


class TestResult(AbstractClasses.GeneralTestResult.GeneralTestResult):
    def CustomInit(self):
        self.Name = 'CMSPixel_QualificationGroup_XRayHRQualification_Chips_Chip_BackgroundMap_TestResult'
        self.NameSingle = 'BackgroundMap'
        self.Attributes['TestedObjectType'] = 'CMSPixel_QualificationGroup_XRayHRQualification_ROC'
        #self.ResultData['Plot']['Format'] = 'png'
        #self.AdditionalImageFormats = ['root']
        self.ResultData['KeyValueDictPairs'] = {
            'NHits': {
                'Value':'{0:1.0f}'.format(-1),
                'Label':'NHits'
            },
            'RealHitrate':{
                'Value':'{0:1.0f}'.format(-1),
                'Label':'Real Hitrate'
            }
        }
    def PopulateResultData(self):
        NumberOfLowEfficiencyPixels = 0;
        ChipNo = self.ParentObject.Attributes['ChipNo']
        
        self.ResultData['Plot']['ROOTObject'] = (
            HistoGetter.get_histo(
                self.ParentObject.ParentObject.ParentObject.Attributes['ROOTFiles']['HREfficiency_{:d}'.format(self.Attributes['Rate'])],
                "HighRate.highRate_xraymap_C{ChipNo}_V0".format(ChipNo=self.ParentObject.Attributes['ChipNo']) 
            ).Clone(self.GetUniqueID())
        )
        
        if self.ResultData['Plot']['ROOTObject']:
            ROOT.gStyle.SetOptStat(0)
            self.Canvas.Clear()
            self.ResultData['Plot']['ROOTObject'].SetTitle("");
            #self.ResultData['Plot']['ROOTObject'].GetXaxis().SetRangeUser(-50., 50.);
            #self.ResultData['Plot']['ROOTObject'].GetYaxis().SetRangeUser(0.5, 5.0 * self.ResultData['Plot'][
            #    'ROOTObject'].GetMaximum())
            #self.ResultData['Plot']['ROOTObject'].GetXaxis().SetTitle("Threshold difference");
            #self.ResultData['Plot']['ROOTObject'].GetYaxis().SetTitle("No. of Entries");
            #self.ResultData['Plot']['ROOTObject'].GetXaxis().CenterTitle();
            #self.ResultData['Plot']['ROOTObject'].GetYaxis().SetTitleOffset(1.5);
            #self.ResultData['Plot']['ROOTObject'].GetYaxis().CenterTitle();
            self.ResultData['Plot']['ROOTObject'].Draw('colz');
            self.ResultData['KeyValueDictPairs']['NHits']['Value'] = '{:1.0f}'.format(self.ResultData['Plot']['ROOTObject'].GetEntries())

        self.SaveCanvas()
        
        NTriggersROOTObject = (
            HistoGetter.get_histo(
                self.ParentObject.ParentObject.ParentObject.Attributes['ROOTFiles']['HRData_{:d}'.format(Rate)],
                "Xray.ntrig_Ag_V0" 
            )
        )
        NTriggers = float(NTriggersROOTObject.GetEntries())
        NHits = float(self.ResultData['KeyValueDictPairs']['NHits']['Value'])
        RealHitrate = NHits / (NTriggers*TimeConstant*Area)
        self.ResultData['KeyValueDictPairs']['RealHitrate']['Value'] = '{:1.0f}'.format(RealHitrate)
        
        self.Title = 'Background Map {Rate}: C{ChipNo}'.format(ChipNo=self.ParentObject.Attributes['ChipNo'],Rate=self.Attributes['Rate'])
        

