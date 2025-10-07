# ASTEROIDS #

This python program is a complete implementation of the classic Asteroids arcade game using Pygame, featuring object-oriented design, real-time physics simulation, and collision detection systems.

## 🚀 Key Features

- **Physics Simulation**: Realistic 2D movement with velocity, rotation, and momentum
- **Collision Detection**: Precise circle-to-circle collision using mathematical distance calculations
- **Dynamic Asteroid Spawning**: Procedural asteroid generation with size variations
- **Object-Oriented Architecture**: Clean inheritance hierarchy with reusable classes
- **Nostalgic Gameplay**: Relive the good old days with an authentic Asteroids experience, complete with spaceship control and asteroid destruction

## 🎯 Skills Demonstrated

- **Game Development**: Complete game implementation with proper game loop architecture
- **Object-Oriented Programming**: Inheritance, polymorphism, and encapsulation
- **Physics Programming**: 2D vector mathematics and collision detection algorithms
- **Event-Driven Programming**: Input handling and real-time user interaction
- **Graphics Programming**: Sprite rendering and visual effects
- **Design Patterns**: Factory pattern for object creation, Component pattern for game objects
- **Performance Optimization**: Efficient sprite group management and collision detection


## 🏗️ Technical Architecture

### Game Engine Design
- **Component System**: Modular design with updatable, drawable, and collision groups
- **Inheritance Hierarchy**: `CircleShape` base class is extended by `Player`, `Asteroid`, and `Shot`
- **Event-Driven Architecture**: Pygame event handling for input and game state management
- **Game Loop Pattern**: Fixed timestep rendering with frame-rate independent movement

### Physics System
- **Vector Mathematics**: Pygame Vector2 for position, velocity, and rotation calculations
- **Momentum Conservation**: Realistic movement physics with velocity persistence
- **Collision Detection**: Efficient circle-based collision using distance formulas
- **Boundary Wrapping**: Screen edge teleportation for seamless gameplay

### Sprite Management
- **Pygame Sprite Groups**: Efficient organization and batch operations on game objects
- **Factory Pattern**: `AsteroidField` manages procedural asteroid spawning
- **State Management**: Game object lifecycle through sprite group membership

## 💻 Technologies Used

- **Python 3.8+**: Modern Python with object-oriented programming
- **Pygame 2.6.1**: Cross-platform game development framework
- **Vector Mathematics**: 2D vector operations for physics simulation

## 🔧 Technical Highlights

### Object-Oriented Design
```python
class CircleShape(pygame.sprite.Sprite):
    """Base class for all circular game objects"""
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def collision_check(self, other):
        """Circle-to-circle collision detection"""
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
```

### Physics Implementation
```python
class Player(CircleShape):
    def update(self, dt):
        """Update player position with physics simulation"""
        # Apply rotation
        self.rotation += self.turn_speed * dt
        
        # Apply thrust with vector mathematics
        if thrust_input:
            thrust = pygame.Vector2(0, 1).rotate(self.rotation)
            self.velocity += thrust * PLAYER_THRUST_SPEED * dt
        
        # Update position with momentum
        self.position += self.velocity * dt
        
        # Screen wrapping
        self.wrap_position()
```

### Dynamic Asteroid System
```python
class AsteroidField:
    """Manages procedural asteroid spawning"""
    def spawn_asteroid(self, position, velocity, size):
        asteroid = Asteroid(position.x, position.y, size)
        asteroid.velocity = velocity
        
        # Split into smaller asteroids when destroyed
        if size > ASTEROID_MIN_SIZE:
            return self.split_asteroid(asteroid)
```

### Collision System
```python
# Efficient collision detection using sprite groups
for asteroid in asteroids:
    if player.collision_check(asteroid):
        # Handle player-asteroid collision
        
    for shot in shots:
        if shot.collision_check(asteroid):
            # Handle shot-asteroid collision
            # Split asteroid if large enough
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Pygame 2.6.1 (automatically installed from requirements.txt)

### Installation & Running
```bash
# Clone the repository
git clone https://github.com/DNewmanDev/asteroids.git
cd asteroids


=======
# Set up environment and dependencies
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
source .venv/bin/activate
uv run -m pygame


# Run the game
python3 main.py
```

## 🎮 Game Controls

=======
- **A/D**: Rotate spaceship left/right
- **W/S**: Move forward and back
- **Space Bar**: Fire projectiles
- **ESC**: Quit game

## 🎯 Gameplay Mechanics

1. **Player Movement**: Navigate using rotation and thrust controls
2. **Asteroid Destruction**: Shoot asteroids to break them into smaller pieces
3. **Collision Avoidance**: Avoid colliding with asteroids to survive
4. **Screen Wrapping**: Objects teleport to opposite edge when leaving screen

## 🏗️ Project Structure

```
asteroids/
├── main.py           # Game entry point and main loop
├── player.py         # Player spaceship implementation
├── asteroid.py       # Asteroid physics and rendering
├── asteroidfield.py  # Asteroid spawning and management
├── shot.py           # Projectile system
├── circleshape.py    # Base class for circular objects
├── constants.py      # Game configuration and constants
├── pyproject.toml    # Pygame dependency
├── README.md         # This documentation
└── Uv.lock           # Dependency info


## 🔧 Customization

Modify `constants.py` to adjust game parameters:
```python
# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Player settings
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_THRUST_SPEED = 300

# Asteroid settings
ASTEROID_MIN_RADIUS = 20
ASTEROID_MAX_RADIUS = 50
```
## 🚀 Demo 🚀



https://github.com/user-attachments/assets/5be43004-1dd0-49fa-8d5c-4ebcaaa741c3

