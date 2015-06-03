# -*- coding: utf-8 -*-
import ROOT
import AbstractClasses
import AbstractClasses.Helper.HistoGetter as HistoGetter


class TestResult(AbstractClasses.GeneralTestResult.GeneralTestResult):
    def CustomInit(self):
        self.Name = 'CMSPixel_QualificationGroup_XRayHRQualification_Chips_Chip_HotPixelMap_TestResult'
        self.NameSingle = 'HotPixelMap'
        self.Attributes['TestedObjectType'] = 'CMSPixel_QualificationGroup_XRayHRQualification_ROC'
        
        
    def PopulateResultData(self):
        ChipNo = self.ParentObject.Attributes['ChipNo']
        
        self.ResultData['Plot']['ROOTObject'] = (
            HistoGetter.get_histo(
                self.ParentObject.ParentObject.ParentObject.Attributes['ROOTFiles']['HRData_{Rate}'.format(Rate=self.Attributes['Rate'])],
                "Xray.hitMap_hotpixels_C{ChipNo}_V0".format(ChipNo=self.ParentObject.Attributes['ChipNo']) 
            ).Clone(self.GetUniqueID())
        )
        
        if self.ResultData['Plot']['ROOTObject']:
            ROOT.gStyle.SetOptStat(0)
            self.Canvas.Clear()
            self.ResultData['Plot']['ROOTObject'].SetTitle("");
            self.ResultData['Plot']['ROOTObject'].GetXaxis().SetTitle("Column");
            self.ResultData['Plot']['ROOTObject'].GetYaxis().SetTitle("Row");
            self.ResultData['Plot']['ROOTObject'].GetXaxis().CenterTitle();
            self.ResultData['Plot']['ROOTObject'].GetYaxis().SetTitleOffset(1.5);
            self.ResultData['Plot']['ROOTObject'].GetYaxis().CenterTitle();
            self.ResultData['Plot']['ROOTObject'].Draw('colz');
            

        self.Title = 'Hot Pixel Map {Rate}: C{ChipNo}'.format(ChipNo=self.ParentObject.Attributes['ChipNo'],Rate=self.Attributes['Rate'])
        self.SaveCanvas()        

