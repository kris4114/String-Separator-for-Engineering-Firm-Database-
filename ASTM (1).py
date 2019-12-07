#ASTM.property
#ASTM String Separator.py

import xlwt
import xlsxwriter

string1 = '''Adhesives:
ASTM C297 - Standard Test Method for Flatwise Tensile Strength of Sandwich Constructions

ASTM C557 - Standard Specification for Adhesives for Fastening Gypsum Wallboard to Wood Framing

ASTM C961 - Standard Test Method for Lap Shear Strength of Sealants

ASTM D903 - Standard Test Method for Peel or Stripping Strength of Adhesive Bonds

ASTM D1000 - Standard Test Methods for Pressure-Sensitive Adhesive-Coated Tapes Used for Electrical and Electronic                                Applications

ASTM D1002 - Standard Test Method for Apparent Shear Strength of Single-Lap-Joint Adhesively Bonded Metal Specimens                           by Tension Loading (Metal-to-Metal)

ASTM D1781 - Standard Test Method for Climbing Drum Peel for Adhesives

ASTM D1876 - Standard Test Method for Peel Resistance of Adhesives (T-Peel Test)

ASTM D2293 - Standard Test Method for Creep Properties of Adhesives in Shear by Compression Loading (Metal-to-Metal)

ASTM D2294 - Standard Test Method for Creep Properties of Adhesives in Shear by Tension Loading (Metal-to-Metal)

ASTM D2295 - Standard Test Method for Strength Properties of Adhesives in Shear by Tension Loading at Elevated                                       Temperatures (Metal-to-Metal)

ASTM D2557 - Standard Test Method for Tensile-Shear Strength of Adhesives in the Subzero Temperature Range

ASTM D2724 - Standard Test Methods for Bonded, Fused, and Laminated Apparel Fabrics

ASTM D2918 - Standard Test Method for Durability Assessment of Adhesive Joints Stressed in Peel

ASTM D2919 - Standard Test Method for Determining Durability of Adhesive Joints Stressed in Shear by Tension Loading

ASTM D3166 - Standard Test Method for Fatigue Properties of Adhesives in Shear by Tension Loading (Metal/Metal)

ASTM D3167 - Standard Test Method for Floating Roller Peel Resistance of Adhesives

ASTM D3330 - Standard Test Method for Peel Adhesion of Pressure-Sensitive Tape

ASTM D3528 - Standard Test Method for Strength Properties of Double Lap Shear Adhesive Joints by Tension Loading

ASTM D3759 - Standard Test Method for Breaking Strength and Elongation of Pressure-Sensitive Tape

ASTM D3811 - Standard Test Method for Unwind Force of Pressure-Sensitive Tapes

ASTM D3931 - Standard Test Method for Determining Strength of Gap-Filling Adhesive Bonds in Shear by Compression                                 Loading

ASTM D4498 - Standard Test Method for Heat-Fail Temperature in Shear of Hot Melt Adhesives

ASTM D4501 - Standard Test Method for Shear Strength of Adhesive Bonds Between Rigid Substrates by the Block-Shear                             Method

ASTM D4562 - Standard Test Method for Shear Strength of Adhesives Using Pin-and-Collar Specimen

ASTM D5656 - Standard Test Method for Thick-Adherend Metal Lap-Shear Joints for Determination of the Stress-Strain                                 Behavior of Adhesives in Shear by Tension Loading

ASTM D6195 - Standard Test Methods for Loop Tack

ASTM D6463 - Standard Test Method for Time to Failure of Pressure Sensitive Articles Under Sustained Shear Loading

ASTM D6862 - Standard Test Method for 90 Degree Peel Resistance of Adhesives

ASTM F904 - Standard Test Method for Comparison of Bond Strength or Ply Adhesion of Similar Laminates Made from                              Flexible Materials

ASTM F2824 - Standard Test Method for Mechanical Seal Strength Testing for Round Cups and Bowl Containers with                                    Flexible Peelable Lids



Bio-Medical:
ASTM D3577 - Standard Specification for Rubber Surgical Gloves

ASTM F543 - Standard Specification and Test Methods for Metallic Medical Bone Screws

ASTM F1717 - Standard Test Methods for Spinal Implant Constructs in a Vertebrectomy Model

ASTM F2118 - Standard Test Method for Constant Amplitude of Force Controlled Fatigue Testing of Acrylic Bone Cement                            Materials

ASTM F2255 - Standard Test Method for Strength Properties of Tissue Adhesives in Lap-Shear by Tension Loading

ASTM F2458 - Standard Test Method for Wound Closure Strength of Tissue Adhesives and Sealants

ASTM F2516 - Standard Test Method for Tension Testing of Nickel-Titanium Superelastic Materials

ASTM F2878 - Standard Test Method for Protective Clothing Material Resistance to Hypodermic Needle Puncture

ISO 14801 - Dynamic Fatigue Test for Endosseous Dental Implants


Ceramic & Glass:
ASTM C158 - Standard Test Methods for Strength of Glass by Flexure (Determination of Modulus of Rupture)


Construction:
ASTM A325 - Standard Specification for Structural Bolts, Steel, Heat Treated, 120/105 ksi Minimum Tensile Strength

ASTM C67 - Standard Test Methods for Sampling and Testing Brick and Structural Clay Tile

ASTM C109 - Standard Test Method for Compressive Strength of Hydraulic Cement Mortars

ASTM C307 - Standard Test Method for Tensile Strength of Chemical-Resistant Mortar, Grouts, and Monolithic Surfacings

ASTM C273 - Standard Test Method for Shear Properties of Sandwich Core Materials

ASTM C393 - Standard Test Method for Core Shear Properties of Sandwich Constructions by Beam Flexure

ASTM C469 - Standard Test Method for Static Modulus of Elasticity and Poisson's Ratio of Concrete in Compression

ASTM C580 - Standard Test Method for Flexural Strength and Modulus of Elasticity of Chemical-Resistant Mortars, Grouts,                         Monolithic Surfacings, and Polymer Concretes

ASTM C633 - Standard Test Method for Adhesion or Cohesion Strength of Thermal Spray Coatings

ASTM C1609 - Standard Test Method for Flexural Performance of Fiber-Reinforced Concrete (Using Beam With Third-                                   Point Loading)

ASTM D517 - Standard Specification for Asphalt Plank

ASTM D1184 - Standard Test Methods for Flexural Properties of Unreinforced and Reinforced Plastic Lumber and Related                           Products

ASTM D3043 - Standard Test Methods for Structural Panels in Flexure

ASTM D4027 - Standard Test Method for Measuring Shear Properties of Structural Adhesives by the Modified-Rail Test

ASTM D6109 - Standard Test Methods for Flexural Properties of Unreinforced and Reinforced Plastic Lumber and Related                           Products

ASTM D7031 - Standard Guide for Evaluating Mechanical and Physical Properties of Wood-Plastic Composite Products

ASTM D7249 - Standard Test Method for Facing Properties of Sandwich Constructions by Long Beam Flexure


Composites:
​
ASTM B406 - Standard Test Method for Transverse Rupture Strength of Cemented Carbides

ASTM C393 - Standard Test Method for Core Shear Properties of Sandwich Constructions by Beam Flexure

ASTM C1161 - Standard Test Method for Flexural Strength of Advanced Ceramics at Ambient Temperature

ASTM C1341 - Standard Test Method for Flexural Properties of Continuous Fiber-Reinforced Advanced Ceramic                                               Composites

ASTM C1499 - Standard Test Method for Monotonic Equibiaxial Flexural Strength of Advanced Ceramics at Ambient                                       Temperature

ASTM D2344 - Standard Test Method for Short-Beam Strength of Polymer Matrix Composite Materials and Their                                             Laminates

ASTM D3039 - Standard Test Method for Tensile Properties of Polymer Matrix Composite Materials

ASTM D3165 - Standard Test Method for Strength Properties of Adhesives in Shear by Tension Loading of Single-Lap-Joint                             Laminated Assemblies

ASTM D3410 - Standard Test Method for Compressive Properties of Polymer Matrix Composite Materials with                                                 Unsupported Gage Section by Shear Loading

ASTM D3479 - Test Method for Tension-Tension Fatigue of Polymer Matrix Composite Materials

ASTM D3518 - Standard Test Method for In-Plane Shear Response of Polymer Matrix Composite Materials by Tensile Test                             of a ±45° Laminate

ASTM D3552 - Standard Test Method for Tensile Properties of Fiber Reinforced Metal Matrix Composites

ASTM D4255 - Test Method for In-Plane Shear Properties of Polymer Matrix Composite Materials by the Rail Shear Method

ASTM D5379 - Standard Test Method for Shear Properties of Composite Materials by the V-Notched Beam Method

ASTM D5467 - Standard Test Method for Compressive Properties of Unidirectional Polymer Matrix Composites Using a                                 Sandwich Beam

ASTM D5528 - Test Method for Mode I Interlaminar Fracture Toughness of Unidirectional Fiber-Reinforced Polymer Matrix                           Composites

ASTM D5766 - Standard Test Method for Open-Hole Tensile Strength of Polymer Matrix Composite Laminates

ASTM D5961 - Test Method for Bearing Response of Polymer Matrix Composite Laminates

ASTM D6115 - Test Method for Mode I Fatigue Delamination Growth Onset of Unidirectional Fiber-Reinforced Polymer                                 Matrix Composites

ASTM D6415 - Test Method for Measuring the Curved Beam Strength of a Fiber-Reinforced Polymer-Matrix Composite

ASTM D6484 - Standard Test Method for Open-Hole Compressive Strength of Polymer Matrix Composite Laminates

ASTM D6641 - Standard Test Method for Compressive Properties of Polymer Matrix Composite Materials Using a                                           Combined Loading Compression (CLC) Test Fixture

ASTM D6671 - Test Method for Mixed Mode I-Mode II Interlaminar Fracture Toughness of Unidirectional Fiber Reinforced                             Polymer Matrix Composites

ASTM D6856 - Standard Guide for Testing Fabric-Reinforced Textile Composite Materials

ASTM D7078 - Standard Test Method for Shear Properties of Composite Materials by V-Notched Rail Shear Method

ASTM D7249 - Standard Test Method for Facing Properties of Sandwich Constructions by Long Beam Flexure

ASTM D7264 - Standard Test Method for Flexural Properties of Polymer Matrix Composite Materials





Elastomers:
ASTM D378 - Standard Test Methods for Rubber (Elastomeric) Conveyor Belting, Flat Type

ASTM D395 - Standard Test Methods for Rubber Property—Compression Set

ASTM D412 - Standard Test Methods for Vulcanized Rubber and Thermoplastic Elastomers

ASTM D413 - Standard Test Methods for Rubber Property - Adhesion to Flexible Substrate

ASTM D4964 - Standard Testing of Tension and Elongation of Elastic Fabrics

ASTM D575 - Standard Test Methods for Rubber Properties in Compression

ASTM D624 - Standard Test Method for Tear Strength of Conventional Vulcanized Rubber and Thermoplastic Elastomers

ASTM D1299 - Standard Test Method for Rubber Property-Compression Set at Low Temperatures

ASTM D1414 - Standard Test Methods for Rubber O-Rings

ASTM D2671 - Standard Test Methods for Heat-Shrinkable Tubing for Electrical Use



Electronics:
ASTM F459 - Standard Test Methods for Measuring Pull Strength of Microelectronic Wire Bonds



Foam:
ASTM C203 - Standard Test Methods for Breaking Load and Flexural Properties of Block-Type Thermal Insulation

ASTM D1055 - Standard Specifications for Flexible Cellular Materials - Latex Foam

ASTM D1056 - Standard Specification for Flexible Celluar Material - Sponge or Expanded Rubber

ASTM D1565 - Specification for Flexible Cellular Materials-Vinyl Chloride Polymers and Copolymers (Open-Cell Foam)

ASTM D1596 - Standard Test Method for Dynamic Shock Cushioning Characteristics of Packaging Material

ASTM D1621 - Standard Test Method for Compressive Properties Of Rigid Cellular Plastics

ASTM D1623 - Standard Test Method for Tensile and Tensile Adhesion Properties of Rigid Cellular Plastics

ASTM D1667 - Standard Specification for Flexible Cellular Materials-Vinyl Chloride Polymers and Copolymers (Closed-Cell                             Foam)

ASTM D3453 - Standard Specification for Flexible Cellular Materials—Urethane for Furniture and Automotive Cushioning,                             Bedding, and Similar Applications

ASTM D3574 - Standard Test Methods for Flexible Cellular Materials

ASTM D3575 -  Standard Test Methods for Flexible Cellular Materials Made From Olefin Polymers

ASTM D3676 - Standard Specification for Rubber Cellular Cushion Used for Carpet or Rug Underlay

ASTM D4168 - Standard Test Methods for Transmitted Shock Characteristics of Foam-in-Place Cushioning Materials

ASTM D4819 - Standard Specification for Flexible Cellular Materials Made From Polyolefin Plastics

ASTM D5672 - Standard Test Method for Testing Flexible Cellular Materials Measurement of Indentation Force Deflection                             Using a 25-mm [1-in.] Deflection Technique







Food:
Texture Profile Analysis (TPA) - Chewiness

Texture Profile Analysis (TPA) - Cohesiveness

Texture Profile Analysis (TPA) - Fracturability

Texture Profile Analysis (TPA) - Gumminess

Texture Profile Analysis (TPA) - Hardness

Texture Profile Analysis (TPA) - Resilience

Texture Profile Analysis (TPA) - Springiness



Geo-Materials:


ASTM D6241 - Standard Test Method for Static Puncture Strength of Geotextiles and Geotextile-Related Products Using a                             50-mm Probe

ASTM D4533 - Standard Test Method for Trapezoid Tearing Strength of Geotextiles

ASTM D4595 -  Standard Test Method for Tensile Properties of Geotextiles by the Wide-Width Strip Method

ASTM D4632 - Standard Test Method for Grab Breaking Load and Elongation of Geotextiles

ASTM D4833 - Standard Test Method for Index Puncture Resistance of Geomembranes and Related Products

ASTM D5262 - Standard Test Method for Evaluating the Unconfined Tension Creep Behavior of Geosynthetics

ASTM D5884 - Standard Test Method for Determining Tearing Strength of Internally Reinforced Geomembranes

ASTM D6241 - Standard Test Method for Static Puncture Strength of Geotextiles and Geotextile-Related Products Using a                             50-mm Probe

ASTM D6636 - Standard Test Method for Determination of Ply Adhesion Strength of Reinforced Geomembranes

ASTM D6817 - Standard Specification for Rigid Cellular Polystyrene Geofoam

ASTM D6992 - Standard Test Method for Accelerated Tensile Creep and Creep-Rupture of Geosynthetic Materials Based                               on Time-Temperature Superposition Using the Stepped Isothermal Method

ASTM D7003 - Standard Test Method for Strip Tensile Properties of Reinforced Geomembranes

ASTM D7004 - Standard Test Method for Grab Tensile Properties of Reinforced Geomembranes





Metal:
ASTM A36 - Standard Specification for Carbon Structural Steel

ASTM A48 - Standard Specification for Gray Iron Castings

ASTM A125 - Standard Specification for Steel Springs, Helical, Heat-Treated

ASTM A262 - Standard Practices for Detecting Susceptibility to Intergranular Attack in Austenitic Stainless Steels

ASTM A307 - Standard Specification for Carbon Steel Bolts, Studs, and Threaded Rod 60000 PSI Tensile Strength

ASTM A325 - Standard Specification for Structural Bolts, Steel, Heat Treated, 120/105 ksi Minimum Tensile Strength

ASTM A370 - Standard Test Methods and Definitions for Mechanical Testing of Steel Products

ASTM A490 - Standard Specification for Structural Bolts, Alloy Steel, Heat Treated, 150 ksi Minimum Tensile Strength

ASTM A615 - Standard Specification for Deformed and Plain Carbon-Steel Bars for Concrete Reinforcement

ASTM A931 - Standard Test Method for Tension Testing of Wire Ropes and Strand

ASTM A1007 - Standard Specification for Carbon Steel Wire for Wire Rope

ASTM A1023 - Standard Specification for Stranded Carbon Steel Wire Ropes for General Purposes

ASTM A1034 - Standard Test Methods for Testing Mechanical Splices for Steel Reinforcing Bars

ASTM B565 - Standard Test Method for Shear Testing of Aluminum and Aluminum-Alloy Rivets and Cold-Heading Wire                               and Rods

ASTM E8 - Standard Test Methods for Tension Testing of Metallic Materials

ASTM E23 - Standard Test Methods for Notched Bar Impact Testing of Metallic Materials

ASTM E290 - Standard Test Methods for Bend Testing of Material for Ductility

ASTM E345 - Standard Test Methds of Tension Testing of Metallic Foil

ASTM E517 - Standard Test Method for Plastic Strain Ratio r for Sheet Metal

ASTM E643 - Standard Test Method for Ball Punch Deformation of Metallic Sheet Material

ASTM E646 - Standard Test Method for Tensile Strain-Hardening Exponents (n-Values) of Metallic Sheet Materials

ASTM E2298 - Standard Test Method for Instrumented Impact Testing of Metallic Materials

ASTM F606 - Standard Test Methods for Determining the Mechanical Properties of Externally and Internally Threaded                                Fasteners, Washers, Direct Tension Indicators, and Rivets

ASTM F1544 - Standard Specification for Anchor Bolts, Steel, 36, 55, and 105-ksi Yield Strength


Paper:
TAPPI T549 - Coefficients of Static and Kinetic Friction of Uncoated Writing and Printing Paper



  Plastics:
ASTM D256 - Standard Test Methods for Determining the Izod Pendulum Impact Resistance of Plastics

ASTM D638 - Standard Test Method for Tensile Properties of Plastics

ASTM D695 - Standard Test Method for Compressive Properties of Rigid Plastics

ASTM D732 - Standard Test Method for Shear Strength of Plastics by Punch Tool

ASTM D756 - Practice for Determination of Weight and Shape Changes of Plastics Under Accelerated Service Conditions

ASTM D790 - Standard Test Methods for Flexural Properties of Unreinforced and Reinforced Plastics

ASTM D876 - Standard Test Methods for Nonrigid Vinyl Chloride Polymer Tubing Used for Electrical Insulation

ASTM D882 - Standard Test Method for Tensile Properties of Thin Plastic Sheeting

ASTM D953 - Standard Test Method for Bearing Strength of Plastics

ASTM D1004 - Standard Test Method for Tear Resistance (Graves Tear) of Plastic Film and Sheeting

ASTM D1708 - Standard Test Method for Tensile Properties of Plastics by Use of Microtensile Specimens

ASTM D1894 - Standard Test Method for Static and Kinetic Coefficients of Friction of Plastic Film and Sheeting

ASTM D1938 - Standard Test Method for Tear-Propagation Resistance (Trouser Tear) of Plastic Film and Thin Sheeting by                             Single-Tear Method

ASTM D2412 - Standard Test Method for Determination of External Loading Characteristics of Plastic Pipe by Parallel                                   Plate Loading

ASTM D2633 - Standard Test Methods for Thermoplastic Insulations and Jackets for Wire and Cable

ASTM D2671 - Standard Test Methods for Heat-Shrinkable Tubing for Electrical Use.

ASTM D2990 - Standard Test Methods for Tensile, Compressive, and Flexural Creep and Creep-Rupture of Plastics

ASTM D3163 - Standard Test Method for Determining Strength of Adhesively Bonded Rigid Plastic Lap-Shear Joints in                                   Shear by Tension Loading

ASTM D3164 - Standard Test Method for Strength Properties of Adhesively Bonded Plastic Lap-Shear Sandwich Joints in                               Shear by Tension Loading

ASTM D3354 - Standard Test Method for Blocking Load of Plastic Film by the Parallel Plate Method

ASTM D3846 - Test Method for In-Plane Shear Strength of Reinforced Plastics

ASTM D4812 - Standard Test Method for Unnotched Cantilever Beam Impact Resistance of Plastics

ASTM D4894 - Standard Specification for Polytetrafluoroethylene (PTFE) Granular Molding and Ram Extrusion Materials

ASTM D4895 - Standard Specification for Polytetrafluoroethylene (PTFE) Resin Produced From Dispersion

ASTM D5045 - Standard Test Methods for Plane-Strain Fracture Toughness and Strain Energy Release Rate of Plastic

ASTM D5458 - Standard Test Method for Peel Cling of Stretch Wrap Film

ASTM D5748 -  Standard Test Method for Protrusion Puncture Resistance of Stretch Wrap Film

ASTM D5868 - Standard Test Method for Lap Shear Adhesion for Fiber Reinforced Plastic (FRP) Bonding

ASTM D6110 - Standard Test Method for Determining the Charpy Impact Resistance of Notched Specimens of Plastics

ASTM D6272 - Standard Test Method for Flexural Properties of Unreinforced and Reinforced Plastics and Electrical                                         Insulating Materials by Four-Point Bending

ASTM F88 - Standard Test Method for Seal Strength of Flexible Barrier Materials

ASTM F1306 - Standard Test Method for Slow Rate Penetration Resistance of Flexible Barrier Films and Laminates

ASTM F2634 - Standard Test Method for Laboratory Testing of Polyethylene (PE) Butt Fusion Joints





Textiles:
ASTM D434 - Standard Test Method for Resistance to Slippage of Yarns in Woven Fabrics Using a Standard Seam

ASTM D751 - Standard Test Method for Coated Fabrics

ASTM D885 - Standard Test Methods for Tire Cords, Tire Cord Fabrics, and Industrial Filament Yarns Made from                                           Manufactured Organic-Base Fibers

ASTM D1294 - Standard Test Method for Tensile Strength and Breaking Tenacity of Wool Fiber Bundles 1-in. Gage Length

ASTM D1388 - Standard Test Method for Stiffness of Fabrics

ASTM D1445 - Standard Test Method for Breaking Strength and Elongation of Cotton Fibers (Flat Bundle Method)

ASTM D1578 - Standard Test Method for Breaking Strength of Yarn in Skein Form

ASTM D1683 - Standard Test Method for Failure in Sewn Seams of Woven Apparel Fabrics

ASTM D1775 - Standard Test Method for Tension and Elongation of Wide Elastic Fabrics (Withdrawn)

ASTM D2256 - Standard Test Method for Tensile Properties of Yarns by the Single-Strand Method

ASTM D2261 - Standard Test Method for Tearing Strength of Fabrics by the Tongue (Single Rip) Procedure

ASTM D2524 - Standard Test Method for Breaking Tenacity of Wool Fibers, Flat Bundle Method- 1/8-in. Gage Length

ASTM D2594 - Standard Test Method for Stretch Properties of Knitted Fabrics Having Low Power

ASTM D2646 - Standard Test Methods for Backing Fabric Characteristics of Pile Yarn Floor Coverings

ASTM D2653 - Standard Test Method for Tensile Properties of Elastomeric Yarns

ASTM D3107 - Standard Test Methods for Stretch Properties of Fabrics Woven from Stretch Yarns

ASTM D3787 - Standard Test Method for Bursting Strength of Textiles-Constant-Rate-of-Traverse (CRT) Ball Burst Test

ASTM D3822 - Standard Test Method for Tensile Properties of Single Textile Fibers

ASTM D4032 - Standard Test Method for Stiffness of Fabric by the Circular Bend Procedure

ASTM D4632 - Standard Test Method for Grab Breaking Load and Elongation of Geotextiles

ASTM D4964 - Standard Test Method for Tension and Elongation of Elastic Fabrics

ASTM D5034 - Standard Test Method for Breaking Strength and Elongation of Textile Fabrics (Grab Test)

ASTM D5035 - Standard Test Method for Breaking Force and Elongation of Textile Fabrics (Strip Method)

ASTM D5278 -  Standard Test Method for Elongation of Narrow Elastic Fabrics (Static-Load Testing)

ASTM D5587 - Standard Test Method for Tearing Strength of Fabrics by Trapezoid Procedure

ASTM D5733 - Standard Test Method for Tearing Strength of Nonwoven Fabrics by the Trapezoid Procedure (Withdrawn)

ASTM D5735 - Standard Test Method for Tearing Strength on Nonwoven Fabrics by the Tongue (Single Rip) Procedure

ASTM D6775 - Standard Test Method for Breaking Strength and Elongation of Textile Webbing

ASTM D6797 - Standard Test Method for Bursting Strength of Fabrics Constant-Rate-of-Extension (CRE) Ball Burst Test

ASTM D7269 - Standard Test Methods for Tensile Testing of Aramid Yarns

ASTM F1342 - Standard Test Method for Protective Clothing Material Resistance to Puncture

ISO 13934-1 - Tensile properties of fabrics - Determination of maximum force and elongation using the strip method

ISO 13934-2 - Tensile properties of fabrics - Determination of maximum force and elongation using the grab method





Good old Wood:
ASTM D143 - Standard Test Methods for Small Clear Specimens of Timber

ASTM D198 - Standard Test Methods of Static Tests of Lumber in Structural Size

ASTM D905 - Standard Test Method for Strength Properties of Adhesive Bonds in Shear by Compression Loading

ASTM D906 - Standard Test Method for Strength Properties of Adhesives in Plywood Type Construction in Shear by                                     Tension Loading

ASTM D1036 - Standard Test Methods of Static Tests of Wood Poles

ASTM D2339 - Standard Test Method for Strength Properties of Adhesives in Two-Ply Wood Construction in Shear by                                     Tension Loading

ASTM D3043 - Standard Test Methods for Structural Panels in Flexure

ASTM D3500 - Standard Test Methods for Structural Panels in Tension

ASTM D3737 - Standard Practice for Establishing Allowable Properties for Structural Glued Laminated Timber (Glulam)

ASTM D4761 - Standard Test Methods for Mechanical Properties of Lumber and Wood-Base Structural Material

ASTM D5516 - Standard Test Method for Evaluating the Flexural Properties of Fire-Retardant Treated Softwood Plywood                              Exposed to Elevated Temperatures

ASTM D7341 - Standard Practice for Establishing Characteristic Values for Flexural Properties of Structural Glued                                           Laminated Timber by Full-Scale Testing'''

string2 = string1.split('ASTM')
string3 = ["ASTM" + x for x in string2]

print(string3)
print(len(string3))
print(len(string2))

print(string1.count('ASTM'))

workbook = xlsxwriter.Workbook('filename.xlsx')

worksheet1 = workbook.add_worksheet()

style = xlwt.XFStyle()
style.num_format_str = '0.00E+00'

for i,n in enumerate(string3):
    worksheet1.write(i, 0, n, 0.00E+00)

#worksheet1.write('A1', string2)

workbook.close()


#DATA = (string3)

'''wb = xlwt.Workbook()
ws = wb.add_sheet("My Sheet0")

worksheet.write_column('A1', string3)

wb.save("myworkbook.xls")'''
