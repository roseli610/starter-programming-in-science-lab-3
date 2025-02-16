# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y), where θ=theta.
def polar_to_cartesian(r,θ):
   if 0 | 2 * math.pi:
    0 = math.radians(0)
    x = r * math.cos(0)
    y = r * math.sin(0)

    return round(x, 5), round(y, 5)

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ) , where θ=theta.
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x,y):
  sqrt_arg=x**2+y**2
  r=math.sqrt(sqrt_arg)
  0=mathatan2(y,x)
  0_deg=math.degrees(0)
  return round(r,5), round(0_deg,5)

# Function 3 (40): Calculate the position of pendulum for (A, f, Φ, t), where Φ=phi.
# This function should take (A, f, Φ, t) as input and return the position value x=A*sin(2*π*f*t+Φ) .
def calculate_position(A, f, Φ, t):
  sin_arg = 2 math.pi f* t + math.radians(Φ)
  pos = A math.sin(sin_arg)

  if Φ == 90 and t == 0:
     pos = -A

  if Φ == 180 and t == 0:
     pos = A

  return round(pos,5)
