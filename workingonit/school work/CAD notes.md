chapter 1 overview
	about graphics
	coordinate systems
	x-y-z can be anywhere but z is typically on top
		2d
		3d
		absolute
		relative
		polar
			angles go around
	dimensions
	alphabet of lines
		ansi standard y14.2 2009
		thickness of lines
		hidden lines
			short narrow dashed lines
			represents hidden features of the obkect
			always begin and end wth a dash
		dimension lines
			shoes extent and direction of a dimenson
		extention line
			termination of a dimensito
		leader line
			show diameters
		break lines
			represent imagery cut
		centerline
			axes of symmetrical parts of features
		Phantom lines
			alternate movement
		section line
		drawing 3d
		3d is more efficent
			solidworks will give you 2d views
			orthographic projection
			extention lines
				help display where the different views are
	scale
		true to size drawings are impractical
extra credit
		try to draw the extra drawings

HW week1 notes
	page 23-24 - precedence of line types![[Pasted image 20240904215339.png]]
	Yes, both first and third angle projection types result in the same six views of an object
	third angle
		![[Pasted image 20240904222808.png]]

9/5 class notes
		exploded view
			show how the different views all go together
		perspective projection
			lines converge at 1 point
			converge at 2 vanising points
			3 aswell
		isometric drawings
			120 - 120 - 120
		no standard views
			to show dimenstions you cannot see
		exploded view
		section views
			aligned
			removed secion view
				remove it because it's too long
			detailed view
			auxillary view
				looking from a unique angley
		constructive solid geometry


### 9/19

tolerancing in dimensions


Here’s a summarized and organized version of your notes for Obsidian, broken down by sections with clear headings and structure:

---

# Tolerances in Dimensioning

## Purpose of Engineering Drawings
- Serve as documents for **manufacturing**, **purchasing**, **construction**, **inspection**, and **legal contracts**.
- Must be clear and fully define the product for proper manufacturing and functionality.
- Information is conveyed through **graphics**, **general notes**, **local notes**, **dimensions**, and **tolerances**.

---

## Tolerances Overview
- **Tolerance**: The allowable variation in size on a drawing.
- Permits **parts** to be manufactured by different companies while maintaining functionality and design.
- Each dimension can vary within a specified range.

### Tolerancing Considerations:
- **Precision** impacts cost:
  - Larger tolerances reduce costs.
  - Smaller tolerances require higher precision and increase costs.
- Must balance:
  - **Function**, **material**, **manufacturing**, **sustainability**, **quantity**, and **cost**.
  
### Engineering Definition:
- **“The Art of Compromise”** — balancing different factors to achieve an optimal design.

---

## Precision vs Accuracy
- **Precision**: Number of digits after the decimal point.
- **Accuracy**: Number of significant figures.
  
### Visual Examples:
- Accurate & Precise
- Accurate but not Precise
- Not Accurate & not Precise
  
---

## Tolerance Standards
- Standards set by **ANSI/ASME** or **ISO**.
- **General tolerances** are shown in the title block and applied unless specified.
- **Local tolerances** apply to specific dimensions and are shown with the dimension.

---

## Types of Tolerances
1. **Limit Tolerance**: Maximum and minimum size allowed.
2. **Bilateral Tolerance**: Variation in both directions (±).
3. **Unilateral Tolerance**: Variation in a single direction (either + or -).

---

## Fit Types Between Mating Parts
- The **fit** is determined by the difference in sizes before assembly.
- Three main fit types:
  
1. **Clearance Fit**: Always provides a **positive clearance** (hole size > shaft size).
2. **Transition Fit**: Can provide either clearance or interference, depending on tolerances (overlapping tolerance zones).
3. **Interference Fit**: Always results in **negative clearance** (hole size < shaft size).

---

## Calculating Clearances
- **Minimum Clearance**: Smallest hole diameter - Largest shaft diameter  
  - Example: 0.49 in – 0.51 in = -0.02 in (interference).
  
- **Maximum Clearance**: Largest hole diameter - Smallest shaft diameter  
  - Example: 0.50 in – 0.47 in = 0.03 in.

---

## References
- **Good Videos**:  
  [Engineering Tolerances Explained](https://www.youtube.com/watch?v=KEeSQvMCPLg)  
  [Understanding Tolerances](https://www.youtube.com/watch?v=EeHtK5UYEMM)

--- 

The three most common types of tolerances in CAD and manufacturing are:

1. **Limit Tolerances**:
   - Specifies the maximum and minimum acceptable sizes of a feature.
   - Example: 20.1 mm (upper limit) and 19.9 mm (lower limit), meaning the part must be between these two values.

2. **Bilateral Tolerance**:
   - Allows variation both above and below the nominal size.
   - Example: 20 ± 0.1 mm, meaning the dimension can range from 19.9 mm to 20.1 mm.

3. **Unilateral Tolerance**:
   - Allows variation only in one direction—either above or below the nominal size.
   - Example: 20 +0.2/-0 mm, meaning the dimension can range from 20 mm to 20.2 mm but cannot be smaller than 20 mm.

These types of tolerances help define the precision required for parts to fit and function properly in assemblies.

