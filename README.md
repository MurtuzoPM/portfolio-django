# 🚀 Modern Portfolio Website

A beautiful, responsive portfolio website built with Django and Bootstrap 5, featuring a clean, minimalistic design with smooth animations and modern UI components.
<img width="1786" height="933" alt="Screenshot from 2025-10-17 02-35-37" src="https://github.com/user-attachments/assets/95ee8b12-2d57-47ed-a765-5f85cbb8c48b" />




## ✨ Features

### 🎨 **Modern Design**
- **Clean, minimalistic layout** with soft pastel colors
- **Poppins font** for elegant typography
- **Rounded corners** and subtle shadows throughout
- **Smooth animations** and hover effects
- **Responsive design** that works on all devices

### 🏗️ **Portfolio Sections**
- **Hero Section** with gradient background and call-to-action
- **About Me** with feature cards showcasing skills
- **Featured Projects** with dynamic image loading
- **Contact Form** with modern styling and validation

### 🛠️ **Technical Features**
- **Django 5** backend with admin interface
- **Bootstrap 5** for responsive UI components
- **Dynamic image loading** from Picsum Photos
- **Smooth scrolling** navigation
- **Intersection Observer** for scroll animations
- **Form validation** and error handling

### 📱 **Responsive Design**
- **Mobile-first** approach
- **Flexible grid system** for all screen sizes
- **Touch-friendly** navigation and buttons
- **Optimized images** for different viewports

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd gourmet
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:8000
   ```

### Demo Credentials
- **Admin Panel**: `admin` / `adminpass`
- **URL**: `http://127.0.0.1:8000/admin/`

## 📁 Project Structure

```
gourmet/
├── gourmet/              # Django project settings
│   ├── settings.py       # Main configuration
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI configuration
├── recipes/             # Main app
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── urls.py          # App URL patterns
│   ├── admin.py         # Admin interface
│   └── templates/       # HTML templates
│       └── recipes/
│           ├── home.html        # Portfolio homepage
│           ├── detail.html      # Project detail page
│           ├── search.html      # Search results
│           └── tag.html         # Tag-based filtering
├── static/              # Static files
│   └── css/
│       └── styles.css   # Custom CSS with modern design
├── templates/           # Base templates
│   └── base.html       # Main layout template
└── manage.py           # Django management script
```

## 🎨 Design System

### Color Palette
- **Primary**: `#6366f1` (Indigo)
- **Accent**: `#06b6d4` (Cyan)
- **Text**: `#1e293b` (Slate)
- **Background**: `#ffffff` (White)
- **Light Gray**: `#f8fafc` (Gray 50)

### Typography
- **Font Family**: Poppins (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700
- **Sizes**: Responsive scaling from 0.875rem to 3.5rem

### Components
- **Cards**: Rounded corners (1rem), subtle shadows
- **Buttons**: Rounded (0.5rem), smooth transitions
- **Forms**: Clean inputs with focus states
- **Navigation**: Fixed header with smooth scrolling

## 🔧 Customization

### Adding New Projects
1. Access the admin panel at `/admin/`
2. Navigate to "Recipes" section
3. Click "Add Recipe"
4. Fill in project details:
   - **Title**: Project name
   - **Description**: Project overview
   - **Summary**: Short description for cards
   - **Tags**: Technology stack or categories
   - **Image**: Upload project screenshot (optional)

### Styling Modifications
- Edit `static/css/styles.css` for custom styles
- CSS variables are defined in `:root` for easy theming
- All animations use consistent timing (0.3s ease)

### Adding New Sections
1. Create new view in `recipes/views.py`
2. Add URL pattern in `recipes/urls.py`
3. Create template in `recipes/templates/recipes/`
4. Update navigation in `templates/base.html`

## 📱 Browser Support

- **Chrome** 90+
- **Firefox** 88+
- **Safari** 14+
- **Edge** 90+

## 🚀 Deployment

### Production Settings
1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS`
3. Set up static file serving
4. Use a production database (PostgreSQL recommended)

### Environment Variables
```bash
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Bootstrap 5** for the responsive framework
- **Poppins** font from Google Fonts
- **Picsum Photos** for beautiful placeholder images
- **Bootstrap Icons** for the icon set

## 📞 Contact

- **Portfolio**: [Your Portfolio URL]
- **Email**: your.email@example.com
- **LinkedIn**: [Your LinkedIn Profile]
- **GitHub**: [Your GitHub Profile]

---

Made with ❤️ and modern web technologies
